from pymongo import MongoClient


class MongoUtils:
    def __init__(self):
        pass

    # ==fc== create mongo client from config file
    @staticmethod
    def create_client():
        client = MongoClient("mongodb://localhost:27017/meizitu")
        return client

    @staticmethod
    def findAllLinks(db):
        cursor = db.links.find()
        result = []
        for item in cursor:
            result.append(item['url'])
        return result
