from flask import Flask
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
from flask_apscheduler import APScheduler
import requests
from scraper import Scraper
import json


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__, static_folder='frontend', static_url_path='')
app.config.from_object(Config())

scheduler = APScheduler()


# Schedule a scraper to save internship listing data in csv format
@scheduler.task('interval', id='scrape_listings', seconds=300,
                misfire_grace_time=900)
def seed_db():
    s = Scraper()
    data = s.seed_applications()[8:]
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


scheduler.start()

CORS(app)


@app.route('/internships', methods=['GET'])
@cross_origin()
def index():
    url = 'https://location-splitter-6a8b6f1a4160.herokuapp.com/splitter'
    with open('data.json') as f:
        data = json.load(f)
    res = requests.post(url, json=data)
    with open("data.json", "w") as json_file:
        json.dump(res.json(), json_file, indent=4)
    return res.json()


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()
