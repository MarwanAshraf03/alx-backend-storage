#!/usr/bin/env python3
"""Module"""


def update_topics(mongo_collection, name, topics):
    """returns all documents in a collection"""
    qfind = {"name": name}
    updatef = {"$set": {"topics": topics}}
    mongo_collection.update_one(qfind, updatef)
