import json
from scraper import Scraper


def run_scraper():
    with open('data.json') as f:
        data = json.load(f)
    s = Scraper()
    data = s.seed_applications()
    print(data[:50])


if __name__ == "__main__":
    run_scraper()