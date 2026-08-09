import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from benchmarks.result_contract import (
    BenchmarkContractError,
    SCHEMA_VERSION,
    build_capture,
    collect_result_paths,
    load_payload,
    main,
    records_from_payload,
    require_valid_records,
    validate_paths,
    validate_records,
    write_capture,
)


class BenchmarkResultContractTests(unittest.TestCase):

    def test_direct_and_darrel_records_are_valid(self):
        records = [self.direct_record(), self.darrel_record()]

        self.assertEqual(validate_records(records), [])

    def test_missing_mode_fields_are_rejected(self):
        record = self.direct_record()
        del record["metrics"]

        issues = validate_records([record])

        self.assertTrue(any("missing direct fields" in item for item in issues))
        with self.assertRaises(BenchmarkContractError):
            require_valid_records([record])

    def test_non_finite_numeric_fields_are_rejected(self):
        direct = self.direct_record()
        darrel = self.darrel_record()
        direct["elapsed_seconds"] = float("inf")
        darrel["input_tokens"] = float("nan")

        issues = validate_records([direct, darrel])

        self.assertTrue(
            any(
                "elapsed_seconds must be finite and non-negative" in item
                for item in issues
            )
        )
        self.assertTrue(
            any(
                "input_tokens must be finite and non-negative" in item
                for item in issues
            )
        )

    def test_capture_contains_reproducibility_metadata(self):
        records = [self.direct_record(), self.darrel_record()]
        capture = build_capture(
            records,
            source_commit="abc1234",
            run_id="test-run",
            captured_at="2026-08-09T10:00:00+00:00",
        )

        records[0]["metrics"]["eval_count"] = 999
        records[1]["verification"]["verdict"] = "MUTATED"

        self.assertEqual(capture["schema_version"], SCHEMA_VERSION)
        self.assertEqual(capture["run"]["run_id"], "test-run")
        self.assertEqual(capture["run"]["source_commit"], "abc1234")
        self.assertEqual(capture["run"]["record_count"], 2)
        self.assertEqual(capture["run"]["modes"], ["darrel", "direct"])
        self.assertEqual(len(capture["run"]["prompt_set_sha256"]), 64)
        self.assertNotIn("eval_count", capture["records"][0]["metrics"])
        self.assertEqual(
            capture["records"][1]["verification"]["verdict"],
            "PASS",
        )

    def test_atomic_capture_round_trip(self):
        capture = build_capture(
            [self.direct_record()],
            source_commit="abc1234",
            run_id="round-trip",
            captured_at="2026-08-09T10:00:00+00:00",
        )

        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "capture.json"
            written_path = write_capture(output_path, capture)
            loaded = load_payload(written_path)

        self.assertEqual(loaded, json.loads(json.dumps(capture)))
        self.assertEqual(records_from_payload(loaded), capture["records"])

    def test_write_rejects_raw_record_list(self):
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "capture.json"

            with self.assertRaisesRegex(
                BenchmarkContractError,
                "capture must be an object",
            ):
                write_capture(output_path, [self.direct_record()])

            self.assertFalse(output_path.exists())

    def test_directory_discovery_is_sorted_and_deduplicated(self):
        with tempfile.TemporaryDirectory() as directory:
            result_directory = Path(directory)
            second = result_directory / "b.json"
            first = result_directory / "a.json"
            first.write_text("[]", encoding="utf-8")
            second.write_text("[]", encoding="utf-8")

            discovered = collect_result_paths([
                result_directory,
                second,
            ])

        self.assertEqual(
            [path.name for path in discovered],
            ["a.json", "b.json"],
        )

    def test_validation_summary_is_read_only_for_mixed_results(self):
        with tempfile.TemporaryDirectory() as directory:
            result_directory = Path(directory)
            valid_path = result_directory / "valid.json"
            invalid_path = result_directory / "invalid.json"
            valid_path.write_text(
                json.dumps([self.direct_record()]),
                encoding="utf-8",
            )
            invalid_path.write_text("{}", encoding="utf-8")
            before = {
                path.name: (path.read_bytes(), path.stat().st_mtime_ns)
                for path in (valid_path, invalid_path)
            }

            summary = validate_paths([valid_path, invalid_path])

            after = {
                path.name: (path.read_bytes(), path.stat().st_mtime_ns)
                for path in (valid_path, invalid_path)
            }

        self.assertEqual(summary["status"], "fail")
        self.assertEqual(summary["files_checked"], 2)
        self.assertEqual(summary["files_passed"], 1)
        self.assertEqual(summary["files_failed"], 1)
        self.assertEqual(summary["records_validated"], 1)
        self.assertEqual(before, after)

    def test_json_cli_summary_and_empty_discovery_exit_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            result_directory = Path(directory)
            result_path = result_directory / "run.json"
            result_path.write_text(
                json.dumps([self.direct_record()]),
                encoding="utf-8",
            )
            output = io.StringIO()

            with redirect_stdout(output):
                success_code = main([
                    "--json",
                    str(result_directory),
                ])

            summary = json.loads(output.getvalue())
            empty_directory = result_directory / "empty"
            empty_directory.mkdir()

            with redirect_stdout(io.StringIO()):
                empty_code = main([
                    "--json",
                    str(empty_directory),
                ])

        self.assertEqual(success_code, 0)
        self.assertEqual(summary["status"], "pass")
        self.assertEqual(summary["files_checked"], 1)
        self.assertEqual(empty_code, 2)

    def direct_record(self):
        return {
            "benchmark_version": "v0.2-quality-1",
            "timestamp": "2026-08-09T10:00:00",
            "prompt_id": "M01",
            "category": "analysis",
            "prompt": "Compare two systems.",
            "mode": "direct",
            "provider_requested": "ollama",
            "elapsed_seconds": 1.25,
            "status": "success",
            "provider_actual": "ollama",
            "model": "test-model",
            "fallback_used": False,
            "metrics": {},
            "answer": "Test answer.",
        }

    def darrel_record(self):
        return {
            "benchmark_version": "v0.2-quality-1",
            "timestamp": "2026-08-09T10:00:00",
            "prompt_id": "M02",
            "category": "planning",
            "prompt": "Plan a task.",
            "mode": "darrel",
            "provider_requested": "ollama",
            "elapsed_seconds": 2.5,
            "status": "workspace_complete",
            "provider_actual": ["ollama"],
            "models": ["test-model"],
            "fallback_used": False,
            "complexity": "medium",
            "activated_modules": ["left_reasoning", "verifier"],
            "llm_call_count": 1,
            "input_tokens": 4,
            "output_tokens": 5,
            "prompt_tokens": 0,
            "eval_tokens": 0,
            "answer": "Test answer.",
            "verification": {"verdict": "PASS"},
        }


if __name__ == "__main__":
    unittest.main()
