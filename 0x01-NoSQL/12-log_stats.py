#!/usr/bin/env python3
"""Module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nc = client.logs.nginx
    print(f"{nc.count_documents({})} logs")
    print("Methods:")
    print(f'\tmethod GET: {len(list(nc.find({"method": "GET"})))}')
    print(f'\tmethod POST: {len(list(nc.find({"method": "POST"})))}')
    print(f'\tmethod PUT: {len(list(nc.find({"method": "PUT"})))}')
    print(f'\tmethod PATCH: {len(list(nc.find({"method": "PATCH"})))}')
    print(f'\tmethod DELETE: {len(list(nc.find({"method": "DELETE"})))}')
    cur = nc.find({"method": "GET", "path": "/status"})
    print(f'{len(list(cur))} status check')
