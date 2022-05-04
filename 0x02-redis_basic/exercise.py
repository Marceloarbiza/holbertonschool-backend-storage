#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Optional, Union, Callable


class Cache:
    """ class cache """
    def __init__(self):
        """ init redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store redis """
        redis_key = str(uuid.uuid4())
        self._redis.set(redis_key, data)
        return redis_key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """ get redis """
        g = self._redis.get(key)
        if fn is not None:
            return fn(g)
        return g

    def get_str(self, key: str) -> Optional[str]:
        """ get redis str """
        x = self._redis.get(key)
        return x.decode("utf-8") if x is not None else None

    def get_int(self, key: str) -> Optional[int]:
        """ get redis int """
        x = self._redis.get(key)
        return int(x.decode("utf-8")) if x is not None else None
