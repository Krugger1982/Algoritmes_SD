class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1)- 1
        self.Tree = [None] * tree_size # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        index = 0
        if self.Tree[index] is None or self.Tree[index] == key:
            return index
        if key < self.Tree[index] and len(self.Tree) > 1:       # если ключ меньше проверяемого и дерево не единичный лист (есть потомки)
            return self.FindKeyIndexBranch(1, key)              #      то ищем в левой ветке
        elif key > self.Tree[index] and len(self.Tree) > 1:     # если ключ больше проверяемого и дерево не единичный лист (есть потомки)
            return self.FindKeyIndexBranch(2, key)              #      то ищем в правой ветке
        return None                                             # если ничего не найдено
	
    def FindKeyIndexBranch(self, branch, key):
        # ищем в ветке индекс ключа
        if self.Tree[branch] == key:
            return branch
        elif self.Tree[branch] is None:                                         # если вместо key найдено подходящее место для ключа
            return - branch                                                     # тогда возвращаем отрицательный индекс
        elif self.Tree[branch] > key and branch < (len(self.Tree) - 1) / 2:     # Если уровень не последний и key меньше проверяемого ключа
            return self.FindKeyIndexBranch(2 * branch + 1, key)                 #      то ищем в левой ветке
        elif self.Tree[branch] < key and branch < (len(self.Tree) - 1) / 2:     # Если уровень не последний и key больше проверяемого ключа
            return self.FindKeyIndexBranch(2 * branch + 2, key)                 #      то ищем в правой ветке
        return None                                                             # если ничего не найдено
    
    def AddKey(self, key):
        # добавляем ключ в массив
        index = self.FindKeyIndex(key)
        if index == 0 and self.Tree[index] is None:     # если результат поиска - 0 и дерево пустое
            self.Tree[index] = key
            return index
        elif index is None:         # если нет места для вставки и нет совпадений
            return -1
        elif index < 0:             # если есть место для вставки
            index = -1 * index
            self.Tree[index] = key
            return index
        else:                       # если данный ключ уже есть в дереве (в том числе и на позиции [0])
            return index
