class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1)- 1
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        index = 0
        if self.Tree[index] is None:
            return -len(self.Tree)
        if key == self.Tree[index]:
            return index
        elif key < self.Tree[index] and len(self.Tree) > 1:
            # дополнительно проверяем что находимся не на последнем уровне(то есть есть еще "потомки")
            return self.FindKeyBranch(2 * index + 1, key)
        elif key > self.Tree[index] and len(self.Tree) > 1: 
            return self.FindKeyBranch(2 * index + 2, key)
        return None             # ключ не найден
    
    def FindKeyBranch(self, index, key):
        if self.Tree[index] is None:
        # найден свободный слот
            return -(len(self.Tree) - index)
        if key == self.Tree[index]:
        # найден ключ
            return index
        elif key < self.Tree[index] and index < ((len(self.Tree) + 1) / 2)-1:
            # дополнительно проверяем что находимся не на последнем уровне(то есть существуют еще "потомки")
            return self.FindKeyBranch(2 * index + 1, key)
            # искомый ключ меньше текущего - ищем в "левой" ветке
        elif key > self.Tree[index] and index < ((len(self.Tree) + 1) / 2)-1: 
            return self.FindKeyBranch(2 * index + 2, key)
            # искомый ключ больше текущего - ищем в "правой" ветке
        else:
            return None     # если дошли до последнего уровня (листьев) и ключа там нет, и места для вставки тоже нет

                     
    def AddKey(self, key):
        # добавляем ключ в массив
        index = self.FindKeyIndex(key)
        if index is None:
            return -1; 
            # индекс добавленного/существующего ключа или -1 если не удалось
        elif index < 0:             # если index отрицтельный, значит есть место для вставки ключа
            self.Tree[index] = key  # вставляем ключ
            index = len(self.Tree) + index  # и приводим index к нормальному виду            
        return index
