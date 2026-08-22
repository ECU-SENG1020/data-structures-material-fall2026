

class DsTuple:
    def __init__(self, *args):
        if len(args) == 0:
            raise ValueError
        else:
            self.items = [arg for arg in args]

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        if len(self) == 1:
            return f"({self.items[0]},)"
        else:
            string_items = [str(item) for item in self.items]
            return "(" + ", ".join(string_items) + ")"
        
    def __iter__(self):
        if len(self) == 0:
            return None
        
        index = 0
        while index < len(self.items):
            yield self.items[index]
            index += 1

    # if 4 in my_tuple:
    # value would contain the 4
    def __contains__(self, value):
        for item in self.items:
            if item == value:
                return True
            
        return False
    
    def __getitem__(self, index):
        return self.items[index]     

    def __add__(self,other):
        if(type(other)) != DsTuple:
            return None
        
        new_items = self.items + other.items
        return DsTuple(*new_items)

    def __mul__(self, n):
        new_items = self.items * n  
        return DsTuple(*new_items) 
    
    def count(self, value = None):
        if value == None:
            return 0
        total = 0
        for item in self.items:
            if item == value:
                total += 1

        return total


    def index(self, value):
        if value == None:
            return -1
        index = 0
        for item in self.items:
            if item == value:
                return index
            index += 1

        return -1
    



    
    

    
