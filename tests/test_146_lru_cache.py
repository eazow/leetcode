import importlib

LRUCache = getattr(importlib.import_module("146_lru_cache"), "LRUCache")


def test_lru_cache():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1
    assert cache.get(3) == -1

    cache.put(3, 3)

    assert cache.get(1) == 1
    assert cache.get(2) == -1
    assert cache.get(3) == 3

    cache.put(3, 6)
    assert cache.get(3) == 6
