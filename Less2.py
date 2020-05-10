class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node != None:
            if node.value == val:
                return node
            node = node.next
        return None
    
    def find_all(self, val):
        A = []
        node = self.head
        while node != None:
            if node.value == val:
                A.append(node)
            node = node.next
        return A 
    
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
                    node.next = None                           # ссылка на второй элемент превращается в ссылку на None                 
                    N += 1
                else:                                          # если оба элемента не равны val
                    node = node.next                           # Сдвигаем node и node1 вправо на 1 позицию
                    node1 = node.next                          
                if node.next == None:
                    self.tail = node
                    
    def clean(self):
        self.head = None
        self.tail = None
        
    def len(self):
        node = self.head
        N = 0
        while node != None:
            N += 1
            node = node.next
        return N
    
    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode == None and self.head == None:
            self.head = newNode
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
        elif afterNode == None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            while node != None:
                if node.value == afterNode and node.next == None:
                    node.next = newNode
                    newNode.next = None
                    newNode.prev = node
                    self.tail = newNode
                    break
                elif node.value == afterNode:
                    node1 = node.next
                    node.next = newNode
                    newNode.next = node1
                    newNode.prev = node
                    node1.prev = newNode
                    break
                node = node.next
       
    def add_in_head(self, newNode):
        node = self.head
        if node == None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None            
        else:
            self.head = newNode
            newNode.prev = None
            newNode.next = node
