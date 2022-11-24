from collections import OrderedDict


class LRUCache:
    """
    LRUCache object will be instantiated and called as such:
    obj = LRUCache(capacity)
    val = obj.get(key)
    obj.put(key,value)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = val

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(False)
