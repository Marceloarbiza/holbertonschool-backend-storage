#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union


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
