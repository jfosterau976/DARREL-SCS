import json
import os
import unittest
from unittest.mock import MagicMock, patch

from core.llm_interface import LLMInterface


class AnthropicProviderTests(unittest.TestCase):

    def test_missing_api_key_falls_back_to_ollama(self):

        with patch.dict(
            os.environ,
            {},
            clear=False
        ):
            os.environ.pop(
                "ANTHROPIC_API_KEY",
                None
            )

            interface = LLMInterface(
                provider="anthropic"
            )

            with patch.object(
                LLMInterface,
                "_generate_ollama",
                return_value={
                    "status": "success",
                    "provider": "ollama",
                    "model": "qwen3:1.7b",
                    "response": "Fallback response",
                    "fallback": False,
                    "metrics": {
                        "prompt_eval_count": 10,
                        "eval_count": 4
                    }
                }
            ):

                result = interface.generate(
                    "Test prompt",
                    think=False
                )

        self.assertEqual(
            result.get("status"),
            "success"
        )

        self.assertEqual(
            result.get("requested_provider"),
            "anthropic"
         )

        self.assertEqual(
            result.get("actual_provider"),
            "ollama"
        )

        self.assertTrue(
            result.get("fallback_used")
        )

        self.assertEqual(
            result.get("primary_status"),
            "configuration_error"
        )

        self.assertIn(
            "ANTHROPIC_API_KEY",
            result.get(
                "fallback_reason",
                ""
            )
        )

        self.assertEqual(
            result.get("response"),
            "Fallback response"
        )

    def test_anthropic_success_contract(self):

        mock_payload = {
            "content": [
                {
                    "type": "text",
                    "text": "Claude test response"
                }
            ],
            "usage": {
                "input_tokens": 12,
                "output_tokens": 6
            }
        }

        mock_response = MagicMock()

        mock_response.read.return_value = (
            json.dumps(
                mock_payload
            ).encode("utf-8")
        )

        mock_response.__enter__.return_value = (
            mock_response
        )

        mock_response.__exit__.return_value = (
            False
        )

        with patch.dict(
            os.environ,
            {
                "ANTHROPIC_API_KEY":
                    "test-key"
            }
        ):

            with patch(
                "urllib.request.urlopen",
                return_value=mock_response
            ):

                interface = LLMInterface(
                    provider="anthropic"
                )

                result = interface.generate(
                    "Test prompt",
                    think=False
                )

        self.assertEqual(
            result.get("status"),
            "success"
        )

        self.assertEqual(
            result.get("provider"),
            "anthropic"
        )

        self.assertEqual(
            result.get("response"),
            "Claude test response"
        )

        self.assertFalse(
            result.get("fallback")
        )

        metrics = result.get(
            "metrics",
            {}
        )

        self.assertEqual(
            metrics.get("input_tokens"),
            12
        )

        self.assertEqual(
            metrics.get("output_tokens"),
            6
        )


    def test_anthropic_request_contract(self):

        mock_payload = {
            "content": [
                {
                    "type": "text",
                    "text": "OK"
                }
            ],
            "usage": {}
        }

        mock_response = MagicMock()

        mock_response.read.return_value = (
            json.dumps(
                mock_payload
            ).encode("utf-8")
        )

        mock_response.__enter__.return_value = (
            mock_response
        )

        mock_response.__exit__.return_value = (
            False
        )

        with patch.dict(
            os.environ,
            {
                "ANTHROPIC_API_KEY":
                    "test-key"
            }
        ):

            with patch(
                "urllib.request.urlopen",
                return_value=mock_response
            ) as mocked_urlopen:

                interface = LLMInterface(
                    provider="anthropic"
                )

                interface.generate(
                    "Test prompt"
                )

        request = (
            mocked_urlopen.call_args
            .args[0]
        )

        self.assertEqual(
            request.full_url,
            "https://api.anthropic.com/v1/messages"
        )

        self.assertEqual(
            request.get_method(),
            "POST"
        )

        request_body = json.loads(
            request.data.decode("utf-8")
        )

        self.assertEqual(
            request_body.get("model"),
            interface.model_name
        )

        self.assertEqual(
            request_body.get("max_tokens"),
            1024
        )

        self.assertEqual(
            request_body.get("messages"),
            [
                {
                    "role": "user",
                    "content": "Test prompt"
                }
            ]
        )


if __name__ == "__main__":
    unittest.main()