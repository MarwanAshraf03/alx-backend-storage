#!/usr/bin/env python3
import redis
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data):
        key = str(uuid.uuid4())
        print(type(key))
        print(key)
        return "he"
        self._redis.set(key, data)
        return key