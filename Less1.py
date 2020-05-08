class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head == None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value, end=' ')
            node = node.next

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
        node1 = node.next                              # а второй указатель - на 2й элемент
        N = 0
        if node.value == val and node1 == None:
            self.head = None
            self.tail = None
            N += 1
        if all:
            while node1 != None:
                node1 = node.next
                if  node.value == val:                         # Если 1й элемент - val 
                    self.head = node1                          # Сдвигаем указатель головы на 2й элемент
                    node = node1                               # Ставим указатель node на 2-й элемент
                    node1 = node.next                          # указатель node1  - на  3-й элемент
                elif node1.value == val:                       # Если второй элемент - val
                    node.next = node1.next                     # ссылка на второй жлемент превращается в ссылку на 3й
                    node1 = node.next                          # переменная node принимает значение 3-го элемента
                else:                                          # если оба элемента не равны val
                    node = node.next                           # Сдвигаем node на место 2-го
                    node1 = node.next                          # А node1 на место 3-го
                if node.next == None:
                    self.tail = node
        else:
             while node1 != None and N == 0:
                if  node.value == val:                         # Если 1й элемент - val
                    self.head = node1                          # Сдвигаем указатель головы на 2й элемент
                    node = node1                               # переменная node принимает значение 2-го элемента
                    node1 = node.next                          # переменная node принимает значение 3-го элемента
                    N += 1
                elif node1.value == val:                       # Если второй элемент - val
                    node.next = node1.next                     # ссылка на второй жлемент превращается в ссылку на 3й
                    node1 = node.next                          # переменная node принимает значение 3-го элемента
                    N += 1
                else:                                          # если оба элемента не равны val
                    node = node.next                           # Сдвигаем node на место 2-го
                    node1 = node.next                          # А node1 на место 3-го
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
        C = Node(newNode)
        node = self.head
        if afterNode == None and node == None:
            self.head = C 
            self.tail = C   
        elif afterNode == None:
            C.next = node
            self.head = C   
        else:
            while node != None:
                if node.value == afterNode and node.next == None:
                    node1 = node.next
                    node.next = C
                    C.next = node1
                    self.tail = C
                    break
                elif node.value == afterNode:
                    node1 = node.next
                    node.next = C
                    C.next = node1
                    break
                node = node.next
