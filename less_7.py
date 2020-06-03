class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 != v2:
            return int((v1-v2)/abs(v1-v2))
        return 0
    
    def add(self, value):
        current = Node(value)
        counter = False
        if self.head is None:
            self.head = current
            self.tail = current
        elif self.__ascending:
            Left = self.head
            Right = self.tail
            while counter == False:
                if self.compare(current.value, Left.value) != 1:
                    current.next = Left
                    current.prev = Left.prev
                    Left.prev = current
                    if current.prev is not None:
                        current.prev.next = current
                    else:
                        self.head = current
                    counter = True
                elif self.compare(current.value, Right.value) != -1:
                    current.prev = Right
                    current.next = Right.next
                    Right.next = current
                    if current.next is not None:
                        current.next.prev = current
                    else:
                        self.tail = current
                    counter = True
                else:
                    Right = Right.prev
                    Left = Left.next
        else:
            Left = self.head
            Right = self.tail
            while counter == False:
                if self.compare(current.value, Left.value) != -1:
                    current.next = Left
                    current.prev = Left.prev
                    Left.prev = current
                    if current.prev is not None:
                        current.prev.next = current
                    else:
                        self.head = current
                    counter = True
                elif self.compare(current.value, Right.value) != 1:
                    current.prev = Right
                    current.next = Right.next
                    Right.next = current
                    if current.next is not None:
                        current.next.prev = current
                    else:
                        self.tail = current
                    counter = True
                else:
                    Right = Right.prev
                    Left = Left.next
                    
    def find(self, val):
        if self.__ascending:
            node = self.head
            while node != None:
                if node.value == val:
                    return node
                elif node.value < val:
                    node = node.next
                else:
                    return None
        else:
            node = self.head
            while node != None:
                if node.value == val:
                    return node
                elif node.value > val:
                    node = node.next
                else:
                    return None            
        return None

    def delete(self, val, all=False):
        node = self.head                               # ставим 1й указатель в голову
        if node == None:                               # Из пустого списка ничего нельзя удалить
            return
        N = 0
        if node.value == val and node.next == None:
            self.head = None
            self.tail = None
            N += 1
        if all:
            while node.next != None:
                node1 = node.next
                if  node.value == val:                         # Если 1й элемент - val 
                    self.head = node1                          # Сдвигаем указатель головы на 2й элемент
                    node = node1                               # Ставим указатель node на 2-й элемент
                    node.prev = None
                    node1 = node.next                          # указатель node1  - на  следующий
                elif node1.value == val and node1.next == None: # Если второй элемент - val и он же последний
                    node.next = node1.next                     # ссылка на второй элемент превращается в ссылку на None
                    self.tail = node                           # переменная node становится "хвостом"
                elif node1.value == val:                       # Если второй элемент - val и он не последний
                    node.next = node1.next
                    node1 = node.next
                    node1.prev = node
                else:                                          # если оба элемента не равны val
                    node = node.next                           # Сдвигаем node на место 2-го
                    node1 = node.next                          # А node1 на место 3-го
                if node.next == None:
                    self.tail = node
        else:
             while node.next != None and N == 0:
                node1 = node.next 
                if  node.value == val:                         # Если 1й элемент - val
                    self.head = node1                          # Сдвигаем указатель головы на 2й элемент
                    node = node.next                           # переменная node принимает значение 2-го элемента
                    node.prev = None
                    N += 1
                elif node1.value == val and node1.next == None:  # Если второй элемент - val и он же последний
                    node.next = None                           # ссылка на второй элемент превращается в ссылку на 3й                    
                    N += 1
                elif node1.value == val:
                    node.next = node1.next
                    node1 = node.next
                    node1.prev = node
                    N += 1
                else:                                          # если оба элемента не равны val
                    node = node.next                           # Сдвигаем node и node1 вправо на 1 позицию
                    node1 = node.next                          
                if node.next == None:
                    self.tail = node
                    
    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):
        node = self.head
        N = 0
        while node != None:
            N += 1
            node = node.next
        return N
    
    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() > v2.strip():
            return 1
        elif v1.strip() < v2.strip():
            return -1
        return 0
