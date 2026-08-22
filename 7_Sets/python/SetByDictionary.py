class MySet:
    def __init__(self, *args):
        self.data = {}
        for item in args:
            self.add(item)

    def __str__(self):
        if len(self.data) == 0:
            return "set()"
        else:
            return "{" + ", ".join([str(key) for key in self.data.keys()]) + "}"

    def __len__(self):
        return len(self.data)

    def add(self, value):
        self.data[value] = True  # Use the key to represent the element

    def remove(self, value):
        if value in self.data:
            del self.data[value]

    def __contains__(self, value):
        return value in self.data

    def __iter__(self):
        for key in self.data.keys():
            yield key

    # Union
    def __or__(self, other):
        new_set = MySet()
        for key in self.data.keys():
            new_set.add(key)
        for key in other.data.keys():
            new_set.add(key)
        return new_set

    # Intersection
    def __and__(self, other):
        new_set = MySet()
        for key in self.data.keys():
            if key in other.data:
                new_set.add(key)
        return new_set

    # Difference
    def __sub__(self, other):
        new_set = MySet()
        for key in self.data.keys():
            if key not in other.data:
                new_set.add(key)
        return new_set

    # Copy
    def copy(self):
        new_set = MySet()
        for key in self.data.keys():
            new_set.add(key)
        return new_set