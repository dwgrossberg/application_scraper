from scraper import Scraper
from pymongo_db import PyMongo_DB


def seed_db():
    s = Scraper()
    internships = s.seed_applications()
    p = PyMongo_DB()
    p.insert_docs(internships[8:])


if __name__ == '__main__':
    seed_db()
