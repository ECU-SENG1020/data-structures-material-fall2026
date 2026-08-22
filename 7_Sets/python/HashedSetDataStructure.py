class MyHashedSet:
    def __init__(self):
        self.hashSet = {}
    
    def add(self, value):
        self.hashSet[hash(value)] = value
    
    def remove(self, value):
        if hash(value) in self.hashSet:
            del self.hashSet[hash(value)]
    
    def contains(self, value):
        return hash(value) in self.hashSet
    
    def __iter__(self):
        for i in self.hashSet.values():
            yield i
        return None
    
    def __str__(self):
        if len(self.hashSet) == 0:
            return "set()"
        else:
            return "{" + ", ".join([str(i) for i in self.hashSet.values()]) + "}"