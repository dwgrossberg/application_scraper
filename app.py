from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
from flask_apscheduler import APScheduler
from scraper import Scraper
import csv


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__, static_folder='frontend', static_url_path='')
app.config.from_object(Config())

scheduler = APScheduler()


# Schedule a scraper to save internship listing data in csv format
@scheduler.task('interval', id='scrape_listings', minutes=60,
                misfire_grace_time=900)
def seed_db():
    s = Scraper()
    data = s.seed_applications()[8:]
    with open("data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)

        for row in data:
            csv_writer.writerow([row[0], row[1], row[3], row[2], row[4]])


scheduler.start()

CORS(app)


@app.route('/internships', methods=['GET'])
@cross_origin()
def index():
    data = []
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        data.append(list(csv_reader))
    return jsonify(data)


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()
