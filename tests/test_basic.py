import pytest
from lru_cache import LRUCache, LRUCacheException

def test_basic_put_get():
    cache = LRUCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    assert cache.get('a') == 1
    assert cache.get('b') == 2

def test_eviction():
    cache = LRUCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)  # 'a' should be evicted
    assert cache.get('a') is None
    assert cache.get('b') == 2
    assert cache.get('c') == 3

def test_update_value():
    cache = LRUCache(2)
    cache.put('a', 1)
    cache.put('a', 2)
    assert cache.get('a') == 2

def test_zero_capacity():
    with pytest.raises(LRUCacheException):
        LRUCache(0)

def test_repr():
    cache = LRUCache(2)
    cache.put('x', 10)
    cache.put('y', 20)
    r = repr(cache)
    assert "x" in r and "y" in r
