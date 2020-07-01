class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size       

    def hash_fun(self, key):
        index = 0
        for i in key:
            index += ord(i)
        return index % self.size

    def is_key(self, key):
        return self.slots.count(key) != 0
            
    def put(self, key, value):
        index = self.hash_fun(key)
        N = 0
        K = 0
        while N == 0 and K <= self.size:
            if self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                N += 1
            else:
                index = (index + 1) % self.size
                K += 1

    def get(self, key):
        if self.is_key(key):
            return self.values[self.slots.index(key)]
        else:
            return None
