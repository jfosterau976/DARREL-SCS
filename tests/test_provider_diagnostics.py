import io
import json
import os
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class ProviderDiagnosticsTests(unittest.TestCase):

    def test_diagnostics_are_offline_and_redact_credentials(self):
        from scripts.provider_diagnostics import (
            build_provider_diagnostics,
        )

        secret = "unit-test-secret-must-not-appear"

        with patch.dict(
            os.environ,
            {
                "ANTHROPIC_API_KEY": secret,
                "SCS_LLM_PROVIDER": "anthropic",
            },
            clear=True,
        ):
            with patch("urllib.request.urlopen") as mocked_urlopen:
                diagnostics = build_provider_diagnostics()

        serialized = json.dumps(diagnostics)

        self.assertEqual(diagnostics["active_provider"], "anthropic")
        self.assertTrue(
            diagnostics["providers"]["anthropic"][
                "credential_configured"
            ]
        )
        self.assertFalse(diagnostics["live_checks_performed"])
        self.assertNotIn(secret, serialized)
        mocked_urlopen.assert_not_called()

    def test_cli_output_is_safe_json(self):
        from scripts.provider_diagnostics import main

        output = io.StringIO()

        with patch.dict(os.environ, {}, clear=True):
            with patch("urllib.request.urlopen") as mocked_urlopen:
                with redirect_stdout(output):
                    exit_code = main()

        diagnostics = json.loads(output.getvalue())

        self.assertEqual(exit_code, 0)
        self.assertEqual(diagnostics["active_provider"], "ollama")
        self.assertFalse(
            diagnostics["providers"]["anthropic"][
                "credential_configured"
            ]
        )
        mocked_urlopen.assert_not_called()


if __name__ == "__main__":
    unittest.main()
