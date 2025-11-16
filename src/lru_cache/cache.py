"""
Core LRU Cache implementation using hashmap + doubly linked list.
"""
from typing import Optional, Any
from .exceptions import LRUCacheException

class Node:
    """Doubly linked list node for LRU Cache."""
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

    def __repr__(self):
        return f"Node({self.key!r}, {self.value!r})"

class LRUCache:
    """
    LRU Cache with O(1) get and put operations.
    Evicts least recently used items when capacity is exceeded.
    """
    def __init__(self, capacity: int = 128):
        if capacity <= 0:
            raise LRUCacheException("Capacity must be positive.")
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(None, None)  # Dummy head
        self.tail = Node(None, None)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: Any) -> Optional[Any]:
        node = self.cache.get(key)
        if not node:
            return None
        self._move_to_head(node)
        return node.value

    def put(self, key: Any, value: Any) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                if tail and tail.key in self.cache:
                    del self.cache[tail.key]

    def _add_node(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next
        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev

    def _move_to_head(self, node: Node) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> Optional[Node]:
        node = self.tail.prev
        if node and node != self.head:
            self._remove_node(node)
            return node
        return None

    def __repr__(self):
        items = []
        curr = self.head.next
        while curr and curr != self.tail:
            items.append(f"{curr.key!r}: {curr.value!r}")
            curr = curr.next
        return f"<LRUCache({', '.join(items)})>"
