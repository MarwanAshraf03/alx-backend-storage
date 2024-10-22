#! usr/bin/env python
"""Module"""
import pymongo


def list_all(mongo_collection):
    """returns all documents in a collection"""
    return mongo_collection.find()
