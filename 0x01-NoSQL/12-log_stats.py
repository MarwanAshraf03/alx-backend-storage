#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    print(nginx_collection.count_documents({}))
