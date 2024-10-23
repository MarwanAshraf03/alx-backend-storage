#!/usr/bin/env python3
"""Module"""


def update_topics(mongo_collection, name, topics):
    """returns all documents in a collection"""
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
