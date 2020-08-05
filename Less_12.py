class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size     # массив ключей
        self.values = [None] * self.size    # массив значений
        self.hits = [0] * self.size         # счетчики обращений

    def hash_fun(self, key):
        index = 0
        for i in key:
            index += ord(i)
        return index % self.size

    def is_key(self, key):
        return self.slots.count(key) != 0
            
    def put(self, key, value):
        if self.is_key(key):           # Если такой ключ уже имеется, он перезаписывается
            self.values[self.slots.index(key)] = value
            Vstavleno = True
        else:                           # Если такого ключа нет вставляем новый элемент 
            index = self.hash_fun(key)
            Vstavleno = False
            K = 0
            while not Vstavleno and K <= self.size:
                if self.slots[index] is None:
                    self.slots[index] = key
                    self.values[index] = value
                    Vstavleno = True
                else:
                    index = (index + 1) % self.size
                    K += 1
        if not Vstavleno:               # Если свободных мест не нашлось
        # поиск и очистка наименее ценного слота (с наименьшим количеством обращений)
            Less = self.hits[0]
            current = 0
            for i in range(self.size):
            # пробегаем по всему словарю
                if self.hits[i] < Less:
                    Less = self.hits[i]
                    current = i
                elif self.hits[i] == Less and abs(self.hash_fun(self.slots[i]) - self.hash_fun(key)) < abs(self.hash_fun(self.slots[current]) - self.hash_fun(key)) :
                # при равенстве количества обращений выбираем тот элемент, который ближе по ключу к вставляемому
                    Less = self.hits[i]
                    current = i
            self.slots[current] = key
            self.values[current] = value
            Vstavleno = True
            
    def get(self, key):
        if self.is_key(key):
            self.hits[self.slots.index(key)] += 1
            return self.values[self.slots.index(key)]
        else:
            return None

    def get_hits(self, key):
        if self.is_key(key):
            return self.hits[self.slots.index(key)]
        else:
            return None
