#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient
from pymongo import cursor

def lenn(cur):
    count = 0
    for i in cur:
        # count += 1
        print(i)
    return count

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    print(f'\tmethod GET: {len(list(nginx_collection.find({"method": "GET"})))}')
    print(f'\tmethod POST: {len(list(nginx_collection.find({"method": "POST"})))}')
    print(f'\tmethod PUT: {len(list(nginx_collection.find({"method": "PUT"})))}')
    print(f'\tmethod PATCH: {len(list(nginx_collection.find({"method": "PATCH"})))}')
    print(f'\tmethod DELETE: {len(list(nginx_collection.find({"method": "DELETE"})))}')
    print(f'{len(list(nginx_collection.find({"method": "GET", "path": "/status"})))} status check')
    
# { "_id" : ObjectId("5a8fa9e0d4321e1852684d11"), "path" : "/status", "ip" : "172.31.2.14", "method" : "GET", "date" : "22/Feb/2018:03:51:02" }