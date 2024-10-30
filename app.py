from flask import Flask
from flask_apscheduler import APScheduler
from scraper import Scraper
from pymongo_db import PyMongo_DB
import csv


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()


# Schedule a scraper to save internship listing data in csv format
@scheduler.task('interval', id='scrape_listings', hours=3, 
                misfire_grace_time=900)
def seed_db():
    s = Scraper()
    data = s.seed_applications()[8:]
    with open("data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)

        for row in data:
            csv_writer.writerow([row[0], row[1], row[3], row[2], row[4]])


scheduler.start()


@app.route('/api', methods=['GET'])
def index():
    data = []
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        data.append(list(csv_reader))
    return data


if __name__ == '__main__':
    app.run()
