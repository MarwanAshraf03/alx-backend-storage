#!/usr/bin/env python3
"""Module"""


def schools_by_topic(mongo_collection, topic):
    """returns all documents in a collection"""
    return mongo_collection.find({"topics": {"$in": [topic]}})
