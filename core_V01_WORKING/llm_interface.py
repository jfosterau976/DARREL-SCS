import json
import urllib.request


class LLMInterface:

    def __init__(self, model_name="SCS Local Model", provider="local", model=None):
        self.model_name = model or model_name
        self.provider = provider
        self.url = "http://localhost:11434/api/generate"


    def connect(self):
        return {
            "status": "connected",
            "provider": self.provider,
            "model": self.model_name
        }


    def generate(self, prompt):

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }

        data = json.dumps(payload).encode("utf-8")

        request = urllib.request.Request(
            self.url,
            data=data,
            headers={
                "Content-Type": "application/json"
            }
        )

        try:

            with urllib.request.urlopen(
                request,
                timeout=10
            ) as response:

                raw = response.read().decode("utf-8")
                result = json.loads(raw)

                text = result.get(
                    "response",
                    ""
                )

                if text:
                    return {
                        "response": text
                    }

                return {
                    "response": "",
                    "error": "Empty model response"
                }


        except Exception as error:

            return {
                "response": (
                    "Local model unavailable. "
                    "Using SCS internal reasoning mode."
                ),
                "error": str(error),
                "fallback": True
            }