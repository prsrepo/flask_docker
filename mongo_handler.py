from pymongo import MongoClient


MONGO_HOST = 'localhost'
MONGO_PORT = 27017


class MongoHandler:
    def __init__(self, db_name, collection_name=None):
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = client[db_name]
        if collection_name:
            self.collection = self.db[collection_name]

    def create_doc(self, doc):
        return self.collection.insert_one(doc)

    def read_docs(self, filter_dict):
        return self.collection.find(filter_dict)

    def update_docs(self, filter_dict, update_query):
        return self.collection.update(filter_dict, update_query)

    def remove_docs(self, filter_dict):
        return self.collection.delete_many(filter_dict)

