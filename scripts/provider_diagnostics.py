import json
import os

from core.llm_interface import LLMInterface


SCHEMA_VERSION = "darrel-provider-diagnostics-v0.1"


def build_provider_diagnostics():
    active = LLMInterface()
    ollama = LLMInterface(provider="ollama")
    anthropic = LLMInterface(provider="anthropic")

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "configuration_only",
        "active_provider": active.provider,
        "live_checks_performed": False,
        "credential_values_exposed": False,
        "providers": {
            "ollama": {
                "implementation_available": True,
                "endpoint": ollama.url,
                "endpoint_scope": "localhost",
                "credential_required": False,
                "live_checked": False,
            },
            "anthropic": {
                "implementation_available": True,
                "endpoint": anthropic.url,
                "credential_required": True,
                "credential_configured": bool(
                    os.getenv("ANTHROPIC_API_KEY")
                ),
                "live_checked": False,
            },
        },
        "fallback_policy": {
            "requested_provider": "anthropic",
            "fallback_provider": "ollama",
        },
    }


def main():
    print(
        json.dumps(
            build_provider_diagnostics(),
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
