#!/usr/bin/env python3

"""
This module contains code for the cache class
"""
import redis
from typing import Union


class Cache:
    """
    The Cache class
    """
    def __init__(self):
        """Initialize the object."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis using string as id"""
        import uuid
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
