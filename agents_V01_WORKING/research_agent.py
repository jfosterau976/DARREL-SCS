from plugins.search import search
from plugins.web_browser import web_browser
from core.left_brain import left_brain


class ResearchAgent:
    def __init__(self):
        self.name = "Research Agent"
        self.role = "research"

    def run(self, message):
        search_result = search.search(message)

        if search_result.get("status") != "success":
            return {
                "agent": self.name,
                "status": "search_failed",
                "search": search_result
            }

        sources = search_result.get("results", [])

        if not sources:
            return {
                "agent": self.name,
                "status": "no_sources",
                "sources": []
            }

        first_source = sources[0]

        web_result = web_browser.fetch(
            first_source["url"]
        )

        analysis = left_brain.think(
            f"Analyse this research request carefully and logically:\n"
            f"{message}\n\n"
            f"Source retrieved:\n{web_result}"
        )

        return {
            "agent": self.name,
            "role": self.role,
            "input": message,
            "status": "researched",
            "sources": sources,
            "web_access": web_result,
            "analysis": analysis
        }


research_agent = ResearchAgent()