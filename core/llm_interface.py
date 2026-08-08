import json
import os
import urllib.error
import urllib.request


class LLMInterface:

    def __init__(
        self,
        model_name=None,
        provider="ollama"
    ):
        self.model_name = (
            model_name
            or os.getenv("SCS_LLM_MODEL")
            or "qwen3:1.7b"
        )

        self.provider = provider
        self.url = "http://127.0.0.1:11434/api/generate"

    def connect(self):

        return {
            "status": "configured",
            "provider": self.provider,
            "model": self.model_name,
            "url": self.url
        }

    def generate(self, prompt):

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.4
            }
        }

        request = urllib.request.Request(
            self.url,
            data=json.dumps(payload).encode("utf-8"),
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

                raw = response.read().decode("utf-8")
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
                    "error": "Ollama returned an empty response.",
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