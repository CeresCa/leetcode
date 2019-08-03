class Node:
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 0:
            capacity = 0
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.size = 0

    def _delete_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def _insert_to_first(self, node):
        node.next = self.head.next
        node.pre = self.head
        node.next.pre = node
        self.head.next = node

    def _move_to_first(self, node):
        self._delete_node(node)
        self._insert_to_first(node)

    def get(self, key: int) -> int:
        if self.cache.get(key) is None:
            return -1
        else:
            node = self.cache.get(key)
            self._move_to_first(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self._move_to_first(node)
        else:
            self.size += 1
            node = Node(key, value)
            self.cache[key] = node
            if self.size > self.capacity:
                del self.cache[self.tail.pre.key]
                self._delete_node(self.tail.pre)
            self._insert_to_first(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
