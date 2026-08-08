import json
import os
import urllib.error
import urllib.request


class LLMInterface:

    def __init__(
        self,
        model_name=None,
        provider=None
    ):
        self.provider = (
            provider
            or os.getenv("SCS_LLM_PROVIDER")
            or "ollama"
        ).lower()

        if self.provider == "anthropic":
            self.model_name = (
                model_name
                or os.getenv("SCS_CLAUDE_MODEL")
                or "claude-sonnet-4-20250514"
            )

            self.url = (
                "https://api.anthropic.com/v1/messages"
            )

        else:
            self.provider = "ollama"

            self.model_name = (
                model_name
                or os.getenv("SCS_LLM_MODEL")
                or "qwen3:1.7b"
            )

            self.url = (
                "http://127.0.0.1:11434/api/generate"
            )


    def connect(self):

        return {
            "status": "configured",
            "provider": self.provider,
            "model": self.model_name,
            "url": self.url
        }


    def generate(
        self,
        prompt,
        think=None
    ):

        if self.provider == "anthropic":
            return self._generate_anthropic(
                prompt
            )

        return self._generate_ollama(
            prompt,
            think=think
        )


    def _generate_ollama(
        self,
        prompt,
        think=None
    ):

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.4
            }
        }

        if think is not None:
            payload["think"] = think

        request = urllib.request.Request(
            self.url,
            data=json.dumps(
                payload
            ).encode("utf-8"),
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        try:

            with urllib.request.urlopen(
                request,
                timeout=120
            ) as response:

                raw = (
                    response.read()
                    .decode("utf-8")
                )

                result = json.loads(raw)

                text = result.get(
                    "response",
                    ""
                ).strip()

                metrics = {
                    "total_duration": result.get(
                        "total_duration"
                    ),
                    "load_duration": result.get(
                        "load_duration"
                    ),
                    "prompt_eval_count": result.get(
                        "prompt_eval_count"
                    ),
                    "prompt_eval_duration": result.get(
                        "prompt_eval_duration"
                    ),
                    "eval_count": result.get(
                        "eval_count"
                    ),
                    "eval_duration": result.get(
                        "eval_duration"
                    )
                }

                if text:

                    return {
                        "status": "success",
                        "provider": self.provider,
                        "model": self.model_name,
                        "response": text,
                        "fallback": False,
                        "metrics": metrics
                    }

                return {
                    "status": "empty_response",
                    "provider": self.provider,
                    "model": self.model_name,
                    "response": "",
                    "error": (
                        "Ollama returned an "
                        "empty response."
                    ),
                    "fallback": True,
                    "metrics": metrics
                }

        except urllib.error.HTTPError as error:

            return {
                "status": "http_error",
                "provider": self.provider,
                "model": self.model_name,
                "response": "",
                "error": str(error),
                "fallback": True
            }

        except urllib.error.URLError as error:

            return {
                "status": "connection_error",
                "provider": self.provider,
                "model": self.model_name,
                "response": "",
                "error": str(error),
                "fallback": True
            }

        except Exception as error:

            return {
                "status": "error",
                "provider": self.provider,
                "model": self.model_name,
                "response": "",
                "error": str(error),
                "fallback": True
            }


    def _generate_anthropic(
        self,
        prompt
    ):

        api_key = os.getenv(
            "ANTHROPIC_API_KEY"
        )

        if not api_key:

            return {
                "status": "configuration_error",
                "provider": self.provider,
                "model": self.model_name,
                "response": "",
                "error": (
                    "ANTHROPIC_API_KEY is not set."
                ),
                "fallback": True
            }

        payload = {
            "model": self.model_name,
            "max_tokens": 1024,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        request = urllib.request.Request(
            self.url,
            data=json.dumps(
                payload
            ).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01"
            },
            method="POST"
        )

        try:

            with urllib.request.urlopen(
                request,
                timeout=120
            ) as response:

                raw = (
                    response.read()
                    .decode("utf-8")
                )

                result = json.loads(raw)

                content = result.get(
                    "content",
                    []
                )

                text_parts = []

                for block in content:

                    if (
                        block.get("type")
                        == "text"
                    ):
                        text_parts.append(
                            block.get(
                                "text",
                                ""
                            )
                        )

                text = "\n".join(
                    text_parts
                ).strip()

                usage = result.get(
                    "usage",
                    {}
                )

                metrics = {
                    "input_tokens": usage.get(
                        "input_tokens"
                    ),
                    "output_tokens": usage.get(
                        "output_tokens"
                    )
                }

                if text:

                    return {
                        "status": "success",
                        "provider": self.provider,
                        "model": self.model_name,
                        "response": text,
                        "fallback": False,
                        "metrics": metrics
                    }

                return {
                    "status": "empty_response",
                    "provider": self.provider,
                    "model": self.model_name,
                    "response": "",
                    "error": (
                        "Anthropic returned an "
                        "empty response."
                    ),
                    "fallback": True,
                    "metrics": metrics
                }

        except urllib.error.HTTPError as error:

            return {
                "status": "http_error",
                "provider": self.provider,
                "model": self.model_name,
                "response": "",
                "error": str(error),
                "fallback": True
            }

        except urllib.error.URLError as error:

            return {
                "status": "connection_error",
                "provider": self.provider,
                "model": self.model_name,
                "response": "",
                "error": str(error),
                "fallback": True
            }

        except Exception as error:

            return {
                "status": "error",
                "provider": self.provider,
                "model": self.model_name,
                "response": "",
                "error": str(error),
                "fallback": True
            }


llm_interface = LLMInterface()