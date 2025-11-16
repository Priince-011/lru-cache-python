import pytest
import threading
from lru_cache import ThreadSafeLRUCache

def test_threadsafe_basic():
    cache = ThreadSafeLRUCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    assert cache.get('a') == 1
    assert cache.get('b') == 2

def test_threadsafe_eviction():
    cache = ThreadSafeLRUCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    assert cache.get('a') is None
    assert cache.get('b') == 2
    assert cache.get('c') == 3

def test_threadsafe_multi_thread():
    cache = ThreadSafeLRUCache(5)
    def writer():
        for i in range(100):
            cache.put(f'k{i}', i)
    def reader():
        for i in range(100):
            cache.get(f'k{i}')
    threads = [threading.Thread(target=writer) for _ in range(2)] + [threading.Thread(target=reader) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    # Should not deadlock or throw
