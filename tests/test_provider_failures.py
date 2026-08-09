import os
import unittest
import urllib.error
from unittest.mock import MagicMock, patch

from core.llm_interface import LLMInterface


class ProviderFailureTests(unittest.TestCase):

    def mock_response(self, raw):
        response = MagicMock()
        response.read.return_value = raw
        response.__enter__.return_value = response
        response.__exit__.return_value = False
        return response

    def test_connection_error_contract(self):

        interface = LLMInterface()

        with patch(
            "urllib.request.urlopen",
            side_effect=urllib.error.URLError(
                "test connection failure"
            ),
        ):

            result = interface.generate(
                "Test prompt",
                think=False,
            )

        self.assertEqual(
            result.get("status"),
            "connection_error",
        )

        self.assertEqual(
            result.get("provider"),
            "ollama",
        )

        self.assertEqual(
            result.get("response"),
            "",
        )

        self.assertTrue(
            result.get("fallback")
        )

        self.assertIn(
            "test connection failure",
            result.get("error", ""),
        )

    def test_http_error_contract(self):

        interface = LLMInterface()

        http_error = urllib.error.HTTPError(
            url=interface.url,
            code=500,
            msg="test server error",
            hdrs=None,
            fp=None,
        )

        try:
            with patch(
                "urllib.request.urlopen",
                side_effect=http_error,
            ):

                result = interface.generate(
                    "Test prompt",
                    think=False,
                )
        finally:
            http_error.close()

        self.assertTrue(http_error.closed)

        self.assertEqual(
            result.get("status"),
            "http_error",
        )

        self.assertEqual(
            result.get("response"),
            "",
        )

        self.assertTrue(
            result.get("fallback")
        )

        self.assertIn(
            "500",
            result.get("error", ""),
        )

    def test_unexpected_error_contract(self):

        interface = LLMInterface()

        with patch(
            "urllib.request.urlopen",
            side_effect=RuntimeError(
                "test unexpected failure"
            ),
        ):

            result = interface.generate(
                "Test prompt",
                think=False,
            )

        self.assertEqual(
            result.get("status"),
            "error",
        )

        self.assertEqual(
            result.get("response"),
            "",
        )

        self.assertTrue(
            result.get("fallback")
        )

        self.assertIn(
            "test unexpected failure",
            result.get("error", ""),
        )

    def test_timeout_error_contract(self):

        interface = LLMInterface()

        with patch(
            "urllib.request.urlopen",
            side_effect=TimeoutError("test provider timeout"),
        ):
            result = interface.generate("Test prompt", think=False)

        self.assertEqual(result.get("status"), "timeout_error")
        self.assertEqual(result.get("requested_provider"), "ollama")
        self.assertEqual(result.get("actual_provider"), "ollama")
        self.assertFalse(result.get("fallback_used"))
        self.assertIn("test provider timeout", result.get("error", ""))

    def test_malformed_ollama_response_contract(self):

        interface = LLMInterface()
        response = self.mock_response(b"not-json")

        with patch(
            "urllib.request.urlopen",
            return_value=response,
        ):
            result = interface.generate("Test prompt", think=False)

        self.assertEqual(result.get("status"), "malformed_response")
        self.assertEqual(result.get("provider"), "ollama")
        self.assertEqual(result.get("response"), "")
        self.assertFalse(result.get("fallback_used"))

    def test_missing_ollama_response_field_contract(self):

        interface = LLMInterface()
        response = self.mock_response(b"{}")

        with patch(
            "urllib.request.urlopen",
            return_value=response,
        ):
            result = interface.generate("Test prompt", think=False)

        self.assertEqual(result.get("status"), "empty_response")
        self.assertEqual(result.get("response"), "")
        self.assertTrue(result.get("fallback"))
        self.assertFalse(result.get("fallback_used"))

    def test_missing_ollama_token_metrics_contract(self):

        interface = LLMInterface()
        response = self.mock_response(b'{"response": "OK"}')

        with patch(
            "urllib.request.urlopen",
            return_value=response,
        ):
            result = interface.generate("Test prompt", think=False)

        self.assertEqual(result.get("status"), "success")
        self.assertEqual(
            result.get("metrics"),
            {
                "total_duration": None,
                "load_duration": None,
                "prompt_eval_count": None,
                "prompt_eval_duration": None,
                "eval_count": None,
                "eval_duration": None,
            },
        )

    def test_anthropic_fallback_failure_preserves_provider_identity(self):

        interface = LLMInterface(provider="anthropic")

        with patch.object(
            LLMInterface,
            "_generate_anthropic",
            return_value={
                "status": "configuration_error",
                "provider": "anthropic",
                "model": "test-anthropic-model",
                "response": "",
                "error": "simulated primary failure",
                "fallback": True,
            },
        ), patch.object(
            LLMInterface,
            "_generate_ollama",
            return_value={
                "status": "connection_error",
                "provider": "ollama",
                "model": "test-ollama-model",
                "response": "",
                "error": "simulated fallback failure",
                "fallback": True,
            },
        ):
            result = interface.generate("Test prompt", think=False)

        self.assertEqual(result.get("status"), "connection_error")
        self.assertEqual(result.get("requested_provider"), "anthropic")
        self.assertEqual(result.get("actual_provider"), "ollama")
        self.assertTrue(result.get("fallback_used"))
        self.assertEqual(result.get("primary_status"), "configuration_error")
        self.assertEqual(
            result.get("fallback_reason"),
            "simulated primary failure",
        )
        self.assertEqual(
            result.get("error"),
            "simulated fallback failure",
        )

    def test_malformed_anthropic_response_triggers_identified_fallback(self):

        interface = LLMInterface(provider="anthropic")
        response = self.mock_response(b"not-json")

        with patch.dict(
            os.environ,
            {"ANTHROPIC_API_KEY": "test-key"},
        ), patch(
            "urllib.request.urlopen",
            return_value=response,
        ), patch.object(
            LLMInterface,
            "_generate_ollama",
            return_value={
                "status": "success",
                "provider": "ollama",
                "model": "test-ollama-model",
                "response": "Fallback response",
                "fallback": False,
                "metrics": {},
            },
        ):
            result = interface.generate("Test prompt", think=False)

        self.assertEqual(result.get("status"), "success")
        self.assertEqual(result.get("requested_provider"), "anthropic")
        self.assertEqual(result.get("actual_provider"), "ollama")
        self.assertTrue(result.get("fallback_used"))
        self.assertEqual(result.get("primary_status"), "malformed_response")


if __name__ == "__main__":
    unittest.main()
