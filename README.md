# in-memory-lru-cache

A highly efficient, production-grade, in-memory LRU (Least Recently Used) Cache for Python. Implements O(1) get/put, thread-safety, TTL expiry, and more. PyPI-ready, clean, and extensible.

---

## What is an LRU Cache?
An LRU Cache is a data structure that stores a limited number of items and evicts the least recently used item when the cache exceeds its capacity. It is widely used for memory management, web caching, and more.

## Internal Architecture

```
+-------------------+
|    Hash Map       |
+-------------------+
         |   (key <-> node)
         v
+-------------------+
| Doubly Linked List|
+-------------------+
|  [head]<->...<->[tail]  |
+-------------------+
```
- **Hash Map**: O(1) lookup for nodes by key
- **Doubly Linked List**: O(1) insert/remove/move for recency order

## Features
- O(1) get/put
- No OrderedDict
- Thread-safe variant
- TTL (time-to-live) variant
- Count-based eviction (default)
- (Optional) Documented: size-based eviction
- Python 3.8+

## Time & Space Complexity
- get/put: O(1)
- Space: O(N) for N items

## Installation
```bash
pip install in-memory-lru-cache
```

## Usage
### Basic LRU
```python
from lru_cache import LRUCache
cache = LRUCache(2)
cache.put('a', 1)
cache.put('b', 2)
print(cache.get('a'))  # 1
cache.put('c', 3)      # 'b' evicted
print(cache.get('b'))  # None
```

### Thread-Safe LRU
```python
from lru_cache import ThreadSafeLRUCache
cache = ThreadSafeLRUCache(2)
```

### LRU with TTL
```python
from lru_cache import LRUCacheTTL
cache = LRUCacheTTL(2, default_ttl=5)  # seconds
cache.put('a', 1)
```

## Benchmarks
See `/benchmarks` or run `pytest --benchmark-only` (if enabled).

## Roadmap
- [x] Core LRU
- [x] Thread-safe
- [x] TTL
- [ ] Async variant
- [ ] Memory-based eviction
- [ ] Benchmarks
- [ ] GitHub Actions CI

## Contributing
PRs welcome! See [issues](https://github.com/Priince-011/in-memory-lru-cache/issues).



## Build & Publish

1. Build:
```bash
python -m build
```
2. Publish:
```bash
python -m twine upload dist/*
```

---

## Example
See `/examples` for more.