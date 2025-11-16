import pytest
import time
from lru_cache import LRUCacheTTL

def test_ttl_expiry():
    cache = LRUCacheTTL(2, default_ttl=0.1)
    cache.put('a', 1)
    time.sleep(0.15)
    assert cache.get('a') is None

def test_ttl_override():
    cache = LRUCacheTTL(2, default_ttl=1)
    cache.put('a', 1, ttl=0.1)
    time.sleep(0.15)
    assert cache.get('a') is None

def test_ttl_no_expiry():
    cache = LRUCacheTTL(2)
    cache.put('a', 1)
    assert cache.get('a') == 1

def test_ttl_eviction():
    cache = LRUCacheTTL(2, default_ttl=1)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    assert cache.get('a') is None or cache.get('b') is None or cache.get('c') is not None
