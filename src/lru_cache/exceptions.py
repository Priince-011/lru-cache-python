"""
Custom exceptions for LRU Cache package.
"""
class LRUCacheException(Exception):
    """Base exception for LRU Cache errors."""
    pass

class LRUCacheFullException(LRUCacheException):
    """Raised when cache is full and cannot add new items."""
    pass

class LRUCacheKeyError(LRUCacheException, KeyError):
    """Raised when a key is not found in the cache."""
    pass
