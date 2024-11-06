from abc import ABC, abstractmethod


class JobScraper(ABC):
    def __init__(self, search_keywords, location="Brazil"):
        self.search_keywords = search_keywords
        self.location = location

    @abstractmethod
    def fetch_jobs(self):
        pass
