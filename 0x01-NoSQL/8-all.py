#!/usr/bin/env python3
"""Module"""
import pymongo


def list_all(mongo_collection):
    """returns all documents in a collection"""
    return mongo_collection.find()
