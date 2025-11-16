"""
LRU Cache with TTL (time-to-live) expiry.
"""
from typing import Any, Optional
import time
from .cache import Node, LRUCache
from .exceptions import LRUCacheException

class TTLNode(Node):
    def __init__(self, key: Any, value: Any, ttl: Optional[float] = None):
        super().__init__(key, value)
        self.expiry: Optional[float] = time.time() + ttl if ttl else None

    def is_expired(self) -> bool:
        return self.expiry is not None and time.time() > self.expiry

    def __repr__(self):
        return f"TTLNode({self.key!r}, {self.value!r}, expiry={self.expiry})"

class LRUCacheTTL(LRUCache):
    """
    LRU Cache with optional TTL expiry for each item.
    """
    def __init__(self, capacity: int = 128, default_ttl: Optional[float] = None):
        super().__init__(capacity)
        self.default_ttl = default_ttl

    def get(self, key: Any) -> Optional[Any]:
        node = self.cache.get(key)
        if not node:
            return None
        if isinstance(node, TTLNode) and node.is_expired():
            self._remove_node(node)
            del self.cache[key]
            return None
        self._move_to_head(node)
        return node.value

    def put(self, key: Any, value: Any, ttl: Optional[float] = None) -> None:
        node = self.cache.get(key)
        ttl_val = ttl if ttl is not None else self.default_ttl
        if node:
            if isinstance(node, TTLNode):
                node.value = value
                node.expiry = time.time() + ttl_val if ttl_val else None
            else:
                # Replace with TTLNode
                self._remove_node(node)
                node = TTLNode(key, value, ttl_val)
                self.cache[key] = node
                self._add_node(node)
            self._move_to_head(node)
        else:
            new_node = TTLNode(key, value, ttl_val)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                if tail and tail.key in self.cache:
                    del self.cache[tail.key]

    def __repr__(self):
        items = []
        curr = self.head.next
        while curr and curr != self.tail:
            if isinstance(curr, TTLNode) and curr.is_expired():
                curr = curr.next
                continue
            items.append(f"{curr.key!r}: {curr.value!r}")
            curr = curr.next
        return f"<LRUCacheTTL({', '.join(items)})>"
