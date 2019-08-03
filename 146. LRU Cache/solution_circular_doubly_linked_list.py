PREV, NEXT, KEY, RESULT = 0, 1, 2, 3


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = {}
        # circular queue with root
        self.root = []
        self.root[:] = [self.root, self.root, None, None]
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._move_to_front(node)

        return node[RESULT]

    def _delete_node(self, node):
        node[PREV][NEXT] = node[NEXT]
        node[NEXT][PREV] = node[PREV]

    def _insert_to_front(self, node):
        node[NEXT] = self.root
        node[PREV] = self.root[PREV]
        node[PREV][NEXT] = node[NEXT][PREV] = node

    def _move_to_front(self, node):
        self._delete_node(node)
        self._insert_to_front(node)

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            node[RESULT] = value
            self._move_to_front(node)
            return
        self.size += 1
        if self.size > self.capacity:
            # 直接使用 root 节点作为新节点，然后通过将 root[NEXT] 的待删除节点设为新的 root 节点，避免了删除和分配新节点的消耗
            self.root[KEY] = key
            self.root[RESULT] = value
            self._cache[key] = self.root

            self.root = self.root[NEXT]
            del self._cache[self.root[KEY]]
            return

        node = [None, None, key, value]
        self._cache[key] = node
        self._insert_to_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
