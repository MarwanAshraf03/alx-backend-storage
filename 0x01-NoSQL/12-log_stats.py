#!/usr/bin/env python3
""" 12 """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    print(f'\tmethod GET: {len(list(nginx_collection.find(\
        {"method": "GET"})))}')
    print(f'\tmethod POST: {len(list(nginx_collection.find(\
        {"method": "POST"})))}')
    print(f'\tmethod PUT: {len(list(nginx_collection.find(\
        {"method": "PUT"})))}')
    print(f'\tmethod PATCH: {len(list(nginx_collection.find(\
        {"method": "PATCH"})))}')
    print(f'\tmethod DELETE: {len(list(nginx_collection.find(\
        {"method": "DELETE"})))}')
    print(f'{len(list(nginx_collection.find(\
        {"method": "GET", "path": "/status"})))} status check')
