class MapSum(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.prefix_key_map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map[key] = val
        for i in range(1, len(key)+1):
            if key[:i] not in self.prefix_key_map:
                self.prefix_key_map[key[:i]] = set()
            self.prefix_key_map[key[:i]].add(key)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if prefix not in self.prefix_key_map:
            return 0
        keys = self.prefix_key_map[prefix]
        result = 0
        for key in keys:
            result += self.map[key]
        return result


map_sum = MapSum()
map_sum.insert("apple", 3)
assert map_sum.sum("ap") == 3
map_sum.insert("app", 2)
assert map_sum.sum("ap") == 5