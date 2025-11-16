from lru_cache import LRUCache, ThreadSafeLRUCache, LRUCacheTTL
import time
import threading

def basic_example():
    cache = LRUCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    print('a:', cache.get('a'))
    cache.put('c', 3)
    print('b (should be None):', cache.get('b'))


def threadsafe_example():
    cache = ThreadSafeLRUCache(2)
    def writer():
        for i in range(10):
            cache.put(f'k{i}', i)
    def reader():
        for i in range(10):
            print(cache.get(f'k{i}'))
    threads = [threading.Thread(target=writer), threading.Thread(target=reader)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def ttl_example():
    cache = LRUCacheTTL(2, default_ttl=1)
    cache.put('a', 1)
    print('a:', cache.get('a'))
    time.sleep(1.1)
    print('a (expired):', cache.get('a'))

if __name__ == "__main__":
    print("Basic LRU Example:")
    basic_example()
    print("\nThread-Safe LRU Example:")
    threadsafe_example()
    print("\nTTL LRU Example:")
    ttl_example()
