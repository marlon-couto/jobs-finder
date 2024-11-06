from jobs_finder.scraper.adzuna_scraper import AdzunaJobScraper


def get_all_jobs(keywords):
    scrapers = [
        AdzunaJobScraper(keywords)
    ]

    all_jobs = []
    for scraper in scrapers:
        job_list = scraper.fetch_jobs()
        all_jobs.extend(job_list)

    return all_jobs


def main():
    search_keywords = ["backend", "node.js", "python"]
    jobs = get_all_jobs(search_keywords)

    for job in jobs:
        print(f"Title: {job['title']}, Link: {job['link']}")


if __name__ == "__main__":
    main()
