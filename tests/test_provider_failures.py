import unittest
import urllib.error
from unittest.mock import patch

from core.llm_interface import LLMInterface


class ProviderFailureTests(unittest.TestCase):

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

        with patch(
            "urllib.request.urlopen",
            side_effect=http_error,
        ):

            result = interface.generate(
                "Test prompt",
                think=False,
            )

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


if __name__ == "__main__":
    unittest.main()