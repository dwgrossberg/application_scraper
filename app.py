from flask import Flask
from flask_apscheduler import APScheduler
from scraper import Scraper
from pymongo_db import PyMongo_DB


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()


@scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
def seed_db():
    s = Scraper()
    internships = s.seed_applications()
    p = PyMongo_DB()
    p.insert_docs(internships[8:])


scheduler.start()


@app.route('/api', methods=['GET'])
def index():
    return {
        "hi": "bye"
    }


if __name__ == '__main__':
    app.run()
