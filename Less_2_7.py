class Heap:
    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
        self.Size = 0       # хранит размер кучи в зависимости от заданной глубины

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        self.Size = (2 ** depth) - 1
        for i in a:
            if self.Add(i) == -1:       # пытаемся вставить элемент, 
                break                   # если он не вставился, то выходим
        pass
        

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if self.Size == 0:
            return -1                                                                   # если куча пуста
        self.HeapArray[0], self.HeapArray[-1] = self.HeapArray[-1], self.HeapArray[0]   # меняем местами голову и хвост массива
        result = self.HeapArray.pop()                                                   # и обрезаем хвост
        current = 0                                                                     # метка на "Преемника"
        while current < len(self.HeapArray):                                            # двигаем преемника вниз по куче 
            Left = 2 * current + 1
            Right = 2 * current + 2
            if len(self.HeapArray) - 1 >= Right:                            # если есть оба потомка
                if self.HeapArray[Left] > self.HeapArray[Right] and self.HeapArray[current] < self.HeapArray[Left]:     # если левый больше правого и больше "Преемника"
                    self.HeapArray[current], self.HeapArray[Left] = self.HeapArray[Left], self.HeapArray[current]       # то поменяем "Преемника" местами с левым
                    current = Left                                                                                      # и сдвинем счетчик current
                elif self.HeapArray[Right] > self.HeapArray[Left] and self.HeapArray[current] < self.HeapArray[Right]:  # если правый больше левого и больше "Преемника"
                    self.HeapArray[current], self.HeapArray[Right] = self.HeapArray[Right], self.HeapArray[current]     # то поменяем "Преемника" местами с правым
                    current = Right                                                                                     # и сдвинем счетчик current
                else:                               # а если они оба меньше "Преемника"
                    break                           # то это значит, что он встал на свое место
            elif len(self.HeapArray) == Left + 1 and self.HeapArray[current] < self.HeapArray[Left]:            # если есть только один потомок и он больше "Преемника"
                self.HeapArray[current], self.HeapArray[Left] = self.HeapArray[Left], self.HeapArray[current]   # то поменяем "Преемника" местами с левым
                current = Left                                                                                  # и сдвинем счетчик current
            else:                                   # если потомков нет или единственный потомок меньше "Преемника"
                break                               # то это значит, что "current" встал на свое место                
        return result

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if len(self.HeapArray) == self.Size:
            return False                            # если куча вся заполнена
        self.HeapArray.append(key)                  # вставляем очередной ключ в конец массива
        if len(self.HeapArray) == 1:
            return                                  # если это первый элемент, то никуда его двигать не надо
        current = len(self.HeapArray) - 1
        while current > 0 and self.HeapArray[current] > self.HeapArray[(current-1) // 2]:
                                                    # пока ключ текущего узла больше, чем у его родителя:
            self.HeapArray[current],  self.HeapArray[(current-1) // 2] = self.HeapArray[(current-1) // 2], self.HeapArray[current]
                                                    # то меняем его с родителем
            current = (current-1) // 2              # и сдвигаем метку current
        return True
