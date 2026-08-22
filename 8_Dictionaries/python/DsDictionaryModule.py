class DsDictionaryView:
    def __init__(self, store, view_type):
        self.__store = store
        self.__view_type = view_type
    
    def __str__(self):

        # dict_keys(['a', 'b', 'c', 'd'])
        # dict_values([1, 2, 3, 4])
        # dict_items([('a', 1), ('b', 2)])

        match self.__view_type:
            case "keys":
                return f"{self.__class__.__name__}_Keys({[key for key, _ in self.__store]})"
            case "values":
                return f"{self.__class__.__name__}_Values({[value for _, value in self.__store]})"
            case "items":
                return f"{self.__class__.__name__}_Items({[(key, value) for key, value in self.__store]})"

        return f"{self.__class__.__name__}({list(self.__store)})"
    
    def __iter__(self):
        
        match(self.__view_type):
            case "keys":
                return (key for key, _ in self.__store)
            case "values":
                return (value for _, value in self.__store)
            case "items":
                return ((key, value) for key, value in self.__store)
            case _:
                raise ValueError("Invalid view type") 


class DsDictionary:
    def __init__(self, items=None):
        # use object.__setattr__ to avoid our own __setattr__
        # object.__setattr__(self, "_store", [])
        # object.__setattr__(self, "_keys", [])

        self.__store = []

        if items is not None:
            for key, value in items:
                self.__store.append((key, value))

    def __str__(self):
        return "{" + ", ".join(f"{repr(k)}: {repr(v)}" for k, v in self.__store) + "}"
    
    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.__store):
            if k == key:
                self.__store[i] = (key, value)
                return
        self.__store.append((key, value))

    def __getitem__(self, key):
        for k, v in self.__store:
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.__store):
            if k == key:
                del self.__store[i]
                return
        raise KeyError(key)

    def __len__(self):
        return len(self.__store)

    def __iter__(self):
        return (k for k, _ in self.__store)

    def keys(self):
        return DsDictionaryView(self.__store, "keys")

    def values(self):
        return DsDictionaryView(self.__store, "values")

    def items(self):
        return DsDictionaryView(self.__store, "items")
    

