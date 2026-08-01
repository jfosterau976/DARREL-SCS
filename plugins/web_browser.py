import requests


class WebBrowser:
    def __init__(self):
        self.name = "Web Browser"
        self.status = "ready"

    def fetch(self, url):
        try:
            response = requests.get(
                url,
                timeout=10,
                headers={"User-Agent": "Synthetic-Cognitive-System/0.1"}
            )

            return {
                "plugin": self.name,
                "url": url,
                "status": "success",
                "status_code": response.status_code,
                "content_length": len(response.text)
            }

        except requests.RequestException as error:
            return {
                "plugin": self.name,
                "url": url,
                "status": "error",
                "error": str(error)
            }


web_browser = WebBrowser()