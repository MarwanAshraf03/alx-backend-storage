#!/usr/bin/env python3
"""A module for creating cache class using redis database"""
import redis
import uuid
import typing


class Cache:
    """Class cache using redis database"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, float, int]) -> str:
        """stores data using random uuid as a key then returns the key"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
