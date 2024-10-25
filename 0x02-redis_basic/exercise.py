#!/usr/bin/env python3
import redis
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data):
        key = uuid.uuid4()
        self._redis.set(key, data)
        return key