#!/usr/bin/env python3
"""A module for creating cache class using redis database"""
import redis
import uuid
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    @wraps(method)
    def wrapper(self, data):
        self._redis.incr(method.__qualname__)
        return method(self, data)
    return wrapper


def call_history(method: typing.Callable) -> typing.Callable:
    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        out = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", out)
        return out
    return wrapper


class Cache:

    """Class cache using redis database"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
