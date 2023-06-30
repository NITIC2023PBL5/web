import os

import pymongo
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.environ["DB_URI"]
client = pymongo.MongoClient(DB_URI)


class MongoDB:
    def __init__(self, database_name, collection_name):
        self.db = client[database_name]
        self.collection = self.db[collection_name]

    # 新規データ挿入
    def insert_one(self, data):
        return self.collection.insert_one(data)

    # 新規データ複数挿入
    def insert_many(self, data):
        return self.collection.insert_many(data)

    # データ更新
    def update_one(self, filter, update_data):
        return self.collection.update_one(filter, {"$set": update_data}, upsert=True)

    # 単独データ検索
    def find_one(self, filter):
        return self.collection.find_one(filter)

    # データ検索
    def find(self, filter):
        li = []
        for data in self.collection.find(filter):
            li.append(data)
        return li

    # 全データ取得
    def find_all(self):
        li = []
        for data in self.collection.find():
            li.append(data)
        return li

    # データ削除
    def delete_one(self, filter):
        return self.collection.delete_one(filter)
