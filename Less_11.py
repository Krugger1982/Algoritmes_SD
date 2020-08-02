# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        # ваша реализация хранилища
        self.storage = []
        
    def size(self):
        # количество элементов в множестве
        return len(self.storage)

    def put(self, value):
        # механизм вставки на нужное место с учетом размера
        Vstavleno = False
        if self.size() == 0:
            self.storage.append(value)
            Vstavleno = True
        L = 0
        R = self.size() - 1
        if value == self.storage[L] or value == self.storage[R]:
            Vstavleno = True
        elif value < self.storage[L]:
            self.storage.insert(L, value)
            Vstavleno = True
        elif value > self.storage[R]:
            self.storage.append(value)
            Vstavleno = True        
        else:
            while R - L > 1 and not Vstavleno:
                center = int((L + R) / 2)
                if value == self.storage[center]:
                    Vstavleno = True
                elif value < self.storage[center]:
                    R = center
                else:
                    L = center
            if value > self.storage[L] and value < self.storage[R] and not Vstavleno:
                self.storage.insert(R, value)
        # всегда срабатывает

    def get(self, value):
        if self.size() == 0:
            return False
        L = 0
        R = self.size() - 1
        if value == self.storage[L] or value == self.storage[R]:
            return True
        else:
             while R - L > 1:
                center = int((L + R) / 2)
                if value == self.storage[center]:
                    return True
                elif value < self.storage[center]:
                    R = center
                else:
                    L = center
        return False
        # возвращает True если value имеется в множестве,
        # иначе False


    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        if self.get(value):
            self.storage.remove(value)
            return True
        return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        result = PowerSet()
        for i in reversed(self.storage):
            if set2.get(i):
                result.put(i)
        return result

    def union(self, set2):
        # объединение текущего множества и set2
        result = PowerSet()
        for i in self.storage:
            result.put(i)         
        for i in set2.storage:
            result.put(i)
        return result

    def difference(self, set2):
        # разница текущего множества и set2
        result = PowerSet()
        for i in self.storage:
            if not set2.get(i):
                result.put(i)
        return result

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        result = True
        for i in set2.storage:
            result = result and self.get(i)        
        return result
