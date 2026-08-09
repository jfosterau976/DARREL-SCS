import argparse
from copy import deepcopy
import hashlib
import json
import os
import platform
import uuid
from datetime import datetime, timezone
from pathlib import Path


SCHEMA_VERSION = "darrel-benchmark-results-v0.1"

COMMON_FIELDS = {
    "benchmark_version",
    "timestamp",
    "prompt_id",
    "category",
    "prompt",
    "mode",
    "provider_requested",
    "elapsed_seconds",
    "status",
    "provider_actual",
    "fallback_used",
    "answer",
}

MODE_FIELDS = {
    "direct": {
        "model",
        "metrics",
    },
    "darrel": {
        "models",
        "complexity",
        "activated_modules",
        "llm_call_count",
        "input_tokens",
        "output_tokens",
        "prompt_tokens",
        "eval_tokens",
        "verification",
    },
}


class BenchmarkContractError(ValueError):
    pass


def validate_record(record, index=0):
    prefix = f"record[{index}]"
    issues = []

    if not isinstance(record, dict):
        return [f"{prefix} must be an object"]

    missing = sorted(COMMON_FIELDS - set(record))
    if missing:
        issues.append(f"{prefix} missing fields: {', '.join(missing)}")

    mode = record.get("mode")
    if mode not in MODE_FIELDS:
        issues.append(f"{prefix}.mode must be direct or darrel")
    else:
        mode_missing = sorted(MODE_FIELDS[mode] - set(record))
        if mode_missing:
            issues.append(
                f"{prefix} missing {mode} fields: "
                + ", ".join(mode_missing)
            )

    for field in (
        "benchmark_version",
        "timestamp",
        "prompt_id",
        "category",
        "prompt",
        "provider_requested",
        "status",
    ):
        value = record.get(field)
        if field in record and (
            not isinstance(value, str) or not value.strip()
        ):
            issues.append(f"{prefix}.{field} must be a non-empty string")

    elapsed = record.get("elapsed_seconds")
    if "elapsed_seconds" in record and (
        isinstance(elapsed, bool)
        or not isinstance(elapsed, (int, float))
        or elapsed < 0
    ):
        issues.append(f"{prefix}.elapsed_seconds must be non-negative")

    if "fallback_used" in record and not isinstance(
        record.get("fallback_used"), bool
    ):
        issues.append(f"{prefix}.fallback_used must be boolean")

    if "answer" in record and not isinstance(record.get("answer"), str):
        issues.append(f"{prefix}.answer must be a string")

    if mode == "direct" and "metrics" in record and not isinstance(
        record.get("metrics"), dict
    ):
        issues.append(f"{prefix}.metrics must be an object")

    if mode == "darrel":
        if "models" in record and not isinstance(record.get("models"), list):
            issues.append(f"{prefix}.models must be a list")
        if "activated_modules" in record and not isinstance(
            record.get("activated_modules"), list
        ):
            issues.append(f"{prefix}.activated_modules must be a list")

        for field in (
            "llm_call_count",
            "input_tokens",
            "output_tokens",
            "prompt_tokens",
            "eval_tokens",
        ):
            value = record.get(field)
            if field in record and (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or value < 0
            ):
                issues.append(f"{prefix}.{field} must be non-negative")

    return issues


def validate_records(records):
    if not isinstance(records, list):
        return ["records must be a list"]

    if not records:
        return ["records must not be empty"]

    issues = []
    for index, record in enumerate(records):
        issues.extend(validate_record(record, index))
    return issues


def require_valid_records(records):
    issues = validate_records(records)
    if issues:
        raise BenchmarkContractError("; ".join(issues))


def records_from_payload(payload):
    if isinstance(payload, list):
        return payload

    if isinstance(payload, dict) and isinstance(payload.get("records"), list):
        return payload["records"]

    raise BenchmarkContractError(
        "result payload must be a record list or a capture object"
    )


def prompt_set_sha256(records):
    prompts = [
        {
            "prompt_id": record.get("prompt_id"),
            "category": record.get("category"),
            "prompt": record.get("prompt"),
        }
        for record in records
    ]
    canonical = json.dumps(
        prompts,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def build_capture(
    records,
    source_commit,
    run_id=None,
    captured_at=None,
):
    require_valid_records(records)

    if not isinstance(source_commit, str) or not source_commit.strip():
        raise BenchmarkContractError("source_commit must be a non-empty string")

    copied_records = deepcopy(records)
    return {
        "schema_version": SCHEMA_VERSION,
        "run": {
            "run_id": run_id or str(uuid.uuid4()),
            "captured_at": captured_at or datetime.now(
                timezone.utc
            ).isoformat(timespec="seconds"),
            "source_commit": source_commit.strip(),
            "python_version": platform.python_version(),
            "record_count": len(copied_records),
            "modes": sorted({record["mode"] for record in copied_records}),
            "providers_requested": sorted({
                record["provider_requested"]
                for record in copied_records
            }),
            "prompt_ids": [
                record["prompt_id"]
                for record in copied_records
            ],
            "prompt_set_sha256": prompt_set_sha256(copied_records),
        },
        "records": copied_records,
    }


def write_capture(path, capture):
    if not isinstance(capture, dict):
        raise BenchmarkContractError("capture must be an object")

    output_path = Path(path)
    records = records_from_payload(capture)
    require_valid_records(records)

    if capture.get("schema_version") != SCHEMA_VERSION:
        raise BenchmarkContractError("capture schema_version is invalid")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = output_path.with_name(
        f".{output_path.name}.{uuid.uuid4().hex}.tmp"
    )

    try:
        temporary_path.write_text(
            json.dumps(capture, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary_path, output_path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()

    return output_path


def load_payload(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate DARREL benchmark result JSON without running it."
    )
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args(argv)

    failed = False
    for raw_path in args.paths:
        path = Path(raw_path)
        try:
            records = records_from_payload(load_payload(path))
            issues = validate_records(records)
        except (OSError, json.JSONDecodeError, BenchmarkContractError) as error:
            issues = [type(error).__name__]

        if issues:
            failed = True
            print(f"FAIL: {path} ({len(issues)} issue(s))")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"PASS: {path} ({len(records)} record(s))")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
