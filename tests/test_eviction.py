import pytest
from lru_cache import LRUCache

def test_count_eviction():
    cache = LRUCache(3)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    cache.put('d', 4)
    assert cache.get('a') is None
    assert cache.get('b') == 2
    assert cache.get('c') == 3 or cache.get('d') == 4

def test_eviction_order():
    cache = LRUCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.get('a')
    cache.put('c', 3)
    assert cache.get('b') is None
    assert cache.get('a') == 1
    assert cache.get('c') == 3
