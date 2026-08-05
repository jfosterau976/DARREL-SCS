import json
import urllib.request


class LLMInterface:

    def __init__(
        self,
        name,
        provider="local",
        model="qwen3:4b"
    ):
        self.name = name
        self.provider = provider
        self.model = model
        self.status = "disconnected"

    def connect(self):

        try:
            request = urllib.request.Request(
                "http://localhost:11434/api/tags",
                method="GET"
            )

            with urllib.request.urlopen(
                request,
                timeout=5
            ) as response:

                if response.status == 200:
                    self.status = "connected"

        except Exception:
            self.status = "disconnected"

        return {
            "name": self.name,
            "provider": self.provider,
            "model": self.model,
            "status": self.status
        }

    def generate(self, prompt):

        payload = json.dumps({
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }).encode("utf-8")

        request = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=payload,
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        try:

            with urllib.request.urlopen(
                request,
                timeout=10
            ) as response:

                raw = response.read().decode(
                    "utf-8"
                )

                data = json.loads(raw)

                result = data.get(
                    "response",
                    ""
                )

                if not result:
                    return {
                        "response": "",
                        "error": "Ollama returned an empty response",
                        "raw": raw
                    }

                return {
                    "response": result
                }

                except Exception as error:
                    return {
                       "response": "Local model unavailable. Using SCS internal reasoning mode.",
                       "error": str(error),
                       "fallback": True
                   }


llm_interface = LLMInterface(
    "Local Qwen Interface",
    "local",
    "qwen3:4b"
)