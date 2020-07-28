class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.slots = [0] * self.filter_len
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        # 17
        index = 0        
        for c in str1:
            code = ord(c)
            index = (17 * index + code) % self.filter_len
        return index

    def hash2(self, str1):
        # 223 
        index = 0        
        for c in str1:
            code = ord(c)
            index = (223 * index + code) % self.filter_len
        return index
    
    def add(self, str1):
        self.slots[self.hash1(str1)] = 1
        self.slots[self.hash2(str1)] = 1
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        return self.slots[self.hash1(str1)] == 1 and self.slots[self.hash2(str1)] == 1
        # проверка, имеется ли строка str1 в фильтре
