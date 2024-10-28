#!/usr/bin/env python3
"""A module for creating cache class using redis database"""
import redis
import uuid
import typing

class Cache:
    """Class cache using redis database"""
    def __init__(self) -> None:
        """Constructor"""
        print(self.store.__qualname__)
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """stores data using random uuid as a key then returns the key"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key):
        pass

    def get_int(self, key):
        pass
