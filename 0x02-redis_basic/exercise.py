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
   
    def get(self, key, fn=None):
        """Retrieve key value from redis db"""
        value = self._redis.get(key)
        print(value)
        if value is None:
            return None
        if fn:
            return fn(value)
        try:
            return self.get_int(value)
        except Exception:
            try:
                return self.get_str(value)
            except Exception:
                return None

    def get_str(self, value: bytes) -> str:
        """Convert byte to regular string"""
        return value.decode("utf-8")

    def get_int(self, value: bytes) -> int:
        """Convert byte to integer"""
        return int(value.decode("utf-8"))

