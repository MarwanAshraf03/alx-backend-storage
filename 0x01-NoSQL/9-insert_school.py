#!/usr/bin/env python3
"""Module"""


def insert_school(mongo_collection, **kwargs):
    """returns all documents in a collection"""
    inst = mongo_collection.insert_one(kwargs)
    return inst._inserted_id
