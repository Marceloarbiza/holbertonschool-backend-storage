#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid


class Cache:

    def __init__(self):
        """ init redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """ store redis """
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)
