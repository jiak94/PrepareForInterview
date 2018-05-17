import collections
class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = collections.OrderedDict()
    
    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1
        
    def put(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.cap:
                self.cache.popitem(last=True)
        self.cache[key] = value