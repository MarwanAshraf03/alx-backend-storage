#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {len(nginx_collection.find({"path": "GET"}))}")
    print(f"\tmethod POST: {0}")
    print(f"\tmethod PUT: {0}")
    print(f"\tmethod PATCH: {0}")
    print(f"\tmethod DELETE: {0}")
    print(f"{0} status check")
    
# { "_id" : ObjectId("5a8fa9e0d4321e1852684d11"), "path" : "/status", "ip" : "172.31.2.14", "method" : "GET", "date" : "22/Feb/2018:03:51:02" }