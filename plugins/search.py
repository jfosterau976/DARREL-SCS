import requests
from urllib.parse import quote_plus, urljoin, urlparse, parse_qs
from bs4 import BeautifulSoup


class Search:
    def __init__(self):
        self.name = "Search"
        self.status = "ready"

    def _clean_url(self, href):
        if href.startswith("//"):
            href = urljoin("https://duckduckgo.com", href)

        parsed = urlparse(href)

        if "duckduckgo.com" in parsed.netloc:
            params = parse_qs(parsed.query)
            if "uddg" in params:
                return params["uddg"][0]

        return href

    def search(self, query):
        url = (
            "https://html.duckduckgo.com/html/?q="
            + quote_plus(query)
        )

        try:
            response = requests.get(
                url,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            soup = BeautifulSoup(response.text, "html.parser")
            results = []

            for item in soup.select(".result"):
                link = item.select_one(".result__a")

                if not link:
                    continue

                title = link.get_text(" ", strip=True)
                href = self._clean_url(link.get("href", ""))

                if title and href.startswith("http"):
                    results.append({
                        "title": title,
                        "url": href
                    })

                if len(results) >= 5:
                    break

            return {
                "plugin": self.name,
                "query": query,
                "status": "success",
                "status_code": response.status_code,
                "results": results
            }

        except requests.RequestException as error:
            return {
                "plugin": self.name,
                "query": query,
                "status": "error",
                "results": [],
                "error": str(error)
            }


search = Search()