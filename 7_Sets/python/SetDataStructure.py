
class MySet:
    def __init__(self):
        self.data = []

    def __str__(self):

        if len(self.data) == 0:
            return "set()"
        else:
            return "{" + ", ".join([str(i) for i in self.data]) + "}"
        
    def __len__(self):
        return len(self.data)

    def add(self, value):
        if value not in self.data:
            self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    def __iter__(self):
        for i in self.data:
            yield i

        return None
    
    def __contains__(self, value):  
        return value in self.data
    
    # union
    def __or__ (self, other):
        new_set = MySet()
        for i in self.data:
            new_set.add(i)
        for i in other.data:
            new_set.add(i)
        return new_set
    
    # intersection
    def __and__(self, other):
        new_set = MySet()
        for i in self.data:
            if i in other.data:
                new_set.add(i)
        return new_set
    
    # difference
    def __sub__(self, other):
        new_set = MySet()
        for i in self.data:
            if i not in other.data:
                new_set.add(i)
        return new_set