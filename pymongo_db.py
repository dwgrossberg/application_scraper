import os
from os.path import join, dirname
from dotenv import load_dotenv
from pymongo import MongoClient


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class PyMongo_DB:
    def __init__(self):
        self.CONNECTION_STRING = os.environ.get("CONNECTION_STRING")

    def get_database(self):
        client = MongoClient(self.CONNECTION_STRING)
        return client['applications-internships']

    def insert_docs(self, internships):
        db = self.get_database()
        internships2025 = db["internships-2025"]

        for internship in internships:
            data = {
                "company": internship[0],
                "position": internship[1],
                "link": internship[3],
                "location": internship[2],
                "date-posted": internship[4],
                "applied": False,
                "online-assessment": False,
                "date-applied": None,
                "interview-round": None,
                "phone-screen": False,
                "referral": False,
                "result": None,
            }
            if internships2025.count_documents({
                "company": internship[0],
                "position": internship[1],
                "link": internship[3],
                "location": internship[2]
            }):
                continue
            internships2025.insert_one(data)
