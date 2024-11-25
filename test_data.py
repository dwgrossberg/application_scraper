from scraper import Scraper
import json

s = Scraper()
data = s.seed_applications()[8:]
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
