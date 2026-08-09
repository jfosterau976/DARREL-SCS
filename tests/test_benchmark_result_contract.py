import json
import tempfile
import unittest
from pathlib import Path

from benchmarks.result_contract import (
    BenchmarkContractError,
    SCHEMA_VERSION,
    build_capture,
    load_payload,
    records_from_payload,
    require_valid_records,
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
