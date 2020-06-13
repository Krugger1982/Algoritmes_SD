class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size   # Содержит собственно список со значениями

    def hash_fun(self, value):
        index = 0
        for i in value:
            index += ord(i)
        return index % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        if self.slots[index] is None:
            return index
        elif index + self.step >= self.size:
            index += self.step
            index = index % self.size
        else:
            index += self.step
        while index != self.hash_fun(value):
            if self.slots[index] is None:
                return index
            elif index + self.step >= self.size:
                index = (index + self.step) % self.size
            else:
                index = index + self.step
        return None
    
    def put(self, value):
        index = self.seek_slot(value)
        if index != None:
            self.slots[index] = value          
        return index

    def find(self, value):
        # находит индекс слота со значением, или None
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index
        elif index + self.step >= self.size:
            index += self.step
            index = index % self.size
        else:
            index += self.step
        while index != self.hash_fun(value):
            if self.slots[index] == value:
                return index
            elif index + self.step >= self.size:
                index = (index + self.step) % self.size
            else:
                index = index + self.step
        return None
