import requests

from .base import JobScraper


class AdzunaJobScraper(JobScraper):
    def __init__(self, search_keywords):
        super().__init__(search_keywords)
        self.app_id = "294b4404"
        self.app_key = "6511bd59fe7c6f1f5fd2440c8c174207"

    def fetch_jobs(self):
        base_url = "https://api.adzuna.com/v1/api/jobs"
        country = "br"
        query = " ".join(self.search_keywords)

        url = f"{base_url}/{country}/search/1"
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "results_per_page": 10,
            "what": query,
            "where": self.location,
            "content-type": "application/json"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            jobs = [
                {
                    "title": job["title"],
                    "link": job["redirect_url"],
                    "location": job.get("location", {}).get("display_name", "N/A"),
                    "company": job.get("company", {}).get("display_name", "N/A"),
                }
                for job in data.get("results", [])
            ]
            return jobs
        else:
            print("Error searching jobs:", response.status_code, response.text)
            return []
