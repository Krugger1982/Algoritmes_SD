import random
import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_find(self):
        list1 = [8, 35, 2, 31, 5, 17, 10]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        C = s_list.find(5)
        self.assertEqual (C.value, 5)         # Проверка элемента - поле value 
        self.assertEqual(C.next.value, 17)      # Проверка  поля next
        self.assertEqual(C.prev.value, 31)      # Проверка  поля prev
        C = s_list.find(10)
        self.assertEqual (C.value, 10)         # Проверка элемента - поле value 
        self.assertEqual(C.next, None)      # Проверка  поля next
        self.assertEqual(C.prev.value, 17)      # Проверка  поля prev
        self.assertEqual(s_list.head.value, 8)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 35)   
        self.assertEqual(s_list.tail.value, 10)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None)    
    
    def test_find_all(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        C = s_list.find_all(5)
        self.assertEqual(4, len(C))
        for i in C:
            self.assertEqual (i.value, 5)         # Проверка количества найденных элементов 
        self.assertEqual(C[0].next.value, 8)      # Проверка каждого элемента: поле value
        self.assertEqual(C[0].prev, None) 
        self.assertEqual(C[1].next.value, 17)     # Проверка каждого элемента: поле next
        self.assertEqual(C[1].prev.value, 31)      # Проверка  поля prev
        self.assertEqual(C[2].next.value, 5)
        self.assertEqual(C[2].prev.value, 2) 
        self.assertEqual(C[3].next, None)
        self.assertEqual(C[3].prev.value, 5) 
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 8)
        self.assertEqual(s_list.head.prev, None) 
        self.assertEqual(s_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev.value, 5) 
        self.assertEqual(s_list.tail.next, None)

    def test_find_all_in_empty_list(self):
        s_list = LinkedList2()
        C = s_list.find_all(5)
        self.assertEqual(C, [])                # На выходе - пустой список

    def test_find_all_wrong(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5]
        s2_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s2_list.add_in_tail(n)
        C = s2_list.find_all(6)        
        self.assertEqual(C, [])                # На выходе - пустой список

    def test_delete_8_False(self):
        list1 = [5, 8, 35, 2, 35, 31, 5, 8, 17, 10, 2, 5, 5]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        A = s_list.find(8)                      # проверка наличия искомого элемента перед удалением
        self.assertEqual(A.value, 8)
        self.assertEqual(A.prev.value, 5)
        self.assertEqual(A.next.value, 35)
        s_list.delete(35, False)
        self.assertEqual(s_list.len(), L - 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 35)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev.value, 5)
        self.assertEqual(s_list.tail.next, None)
        A1 = s_list.find_all(5)                              # проверка отсутствия удаленного элемента в списке
        self.assertEqual(len(A1), 2)

    def test_delete_8_False(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        A = s_list.find(8)                      # проверка наличия искомого элемента перед удалением
        self.assertEqual(A.value, 8)
        self.assertEqual(A.prev.value, 5)
        self.assertEqual(A.next.value, 35)
        s_list.delete(8, False)
        self.assertEqual(s_list.len(), L - 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 35)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev.value, 5)
        self.assertEqual(s_list.tail.next, None)
        A1 = s_list.find(8)                              # проверка отсутствия удаленного элемента в списке
        self.assertEqual(A1, None)
        
    def test_delete_22_False_from_tail(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 10, 22]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        A = s_list.find(22)                      # проверка наличия искомого элемента перед удалением
        self.assertEqual(A.value, 22)
        self.assertEqual(A.prev.value, 10)
        self.assertEqual(A.next, None)
        L = s_list.len()
        s_list.delete(22, False)
        self.assertEqual(s_list.len(), L - 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 8)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.value, 10)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail.prev.value, 17)

    def test_delete_5_alone_unit_True(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(5))
        A = s_list.find(5)                      # проверка наличия искомого элемента перед удалением
        self.assertEqual(A.value, 5)
        self.assertEqual(A.prev, None)
        self.assertEqual(A.next, None)
        s_list.delete(5, True)
                                                # результат - пустой список
        self.assertEqual(s_list.head, None)               
        self.assertEqual(s_list.tail, None)

    def test_delete_5_alone_unit_False(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(5))
        A = s_list.find(5)                      # проверка наличия искомого элемента перед удалением
        self.assertEqual(A.value, 5)
        self.assertEqual(A.prev, None)
        self.assertEqual(A.next, None)
        s_list.delete(5, False)
        # результат - пустой список
        self.assertEqual(s_list.head, None)               
        self.assertEqual(s_list.tail, None)
        
    def test_delete_666_empty_list(self):
        s_list = LinkedList2()
        s_list.delete(666, False)
        # результат - пустой список
        self.assertEqual(s_list.head, None)               
        self.assertEqual(s_list.tail, None)

    def test_clean(self):
        for i in range(1000):
            N = random.randint(0, 15)
            s_list = LinkedList2()
            for i in range(N):
                n = Node(random.randint(1, 9))
                s_list.add_in_tail(n)
            s_list.clean()
            self.assertEqual(s_list.head, None)
            self.assertEqual(s_list.tail, None)
 
    def test_len(self):
        for i in range(1000):
            N = random.randint(0, 30)
            s_list = LinkedList2()
            for i in range(N):
                n = Node(random.randint(1, 9))
                s_list.add_in_tail(n)
            self.assertEqual(N, s_list.len())

    def test_inserting_666_at_the_tail(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 5, 5]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        s_list.insert(None, Node(666))
        C = s_list.find(666)
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(C.value, 666)                # проверка наличия вставленного элемента
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 8)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.value, 666)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev.value, 5)
        self.assertEqual(s_list.tail.next, None)

    def test_inserting_666_after_last_unit(self):
        list1 = [5, 8, 35, 2, 31, 5, 17]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        X = s_list.find(17)
        s_list.insert(X, Node(666))
        C = s_list.find(666)
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(C.value, 666)                # проверка наличия вставленного элемента
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 8)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.value, 666)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev.value, 17)
        self.assertEqual(s_list.tail.next, None)        

    def test_inserting_666_at_the_middle(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 5, 5]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        X = s_list.find(35)
        s_list.insert(X, Node(666))
        C = s_list.find(666)
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(C.value, 666)                # проверка наличия вставленного элемента
        self.assertEqual(C.next.value, 2)             # и что он вставился куда надо
        self.assertEqual(C.prev.value, 35)
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 8)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.tail.prev.value, 5)

    def test_inserting_666_at_the_empty_list(self):
        s_list = LinkedList2()
        L = s_list.len()
        s_list.insert(None, Node(666))  
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 666)        # Проверка указателя head
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next, None)   
        self.assertEqual(s_list.tail.value, 666)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev, None)  
        self.assertEqual(s_list.tail.next, None)

    def test_inserting_666_at_the_alone_unit_list(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(15))
        L = s_list.len()
        X = s_list.find(15)
        s_list.insert(X, Node(666))  
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 15)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 666)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.value, 666)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev.value, 15) 
        self.assertEqual(s_list.tail.next, None)            

    def test_add_in_head_empty_list(self):
        s_list = LinkedList2()
        L = s_list.len()
        s_list.add_in_head(Node(666))
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 666)        # Проверка указателя head
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next, None)   
        self.assertEqual(s_list.tail.value, 666)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev, None)  
        self.assertEqual(s_list.tail.next, None)

    def test_add_in_head(self):        
        list1 = [5, 8, 35, 2, 31, 5, 17, 5, 5]
        s_list = LinkedList2()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        s_list.add_in_head(Node(666))
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 666)        # Проверка указателя head
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next.value, 5)   
        self.assertEqual(s_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s_list.tail.prev.value, 5)  
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.head.next.prev, s_list.head)      # Проверка указателя prev у второго элемента - должен указывать на HEAD
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
