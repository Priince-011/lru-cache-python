"""
Thread-safe LRU Cache implementation.
"""
from typing import Any, Optional
from threading import RLock
from .cache import Node, LRUCache
from .exceptions import LRUCacheException

class ThreadSafeLRUCache(LRUCache):
    """
    Thread-safe LRU Cache using RLock.
    """
    def __init__(self, capacity: int = 128):
        super().__init__(capacity)
        self._lock = RLock()

    def get(self, key: Any) -> Optional[Any]:
        with self._lock:
            return super().get(key)

    def put(self, key: Any, value: Any) -> None:
        with self._lock:
            super().put(key, value)

    def __repr__(self):
        with self._lock:
            return super().__repr__()
