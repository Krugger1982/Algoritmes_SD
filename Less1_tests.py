import random
import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_find_all(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5]
        s1_list = LinkedList()
        for i in list1:
            n = Node(i)
            s1_list.add_in_tail(n)
        C = s1_list.find_all(5)
        self.assertEqual(4, len(C))
        for i in C:
            self.assertEqual (i.value, 5)         # Проверка количества найденных элементов 
        self.assertEqual(C[0].next.value, 8)      # Проверка каждого элемента: поле value
        self.assertEqual(C[1].next.value, 17)     # Проверка каждого элемента: поле next
        self.assertEqual(C[2].next.value, 5)
        self.assertEqual(C[3].next, None)
        self.assertEqual(s1_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s1_list.head.next.value, 8)   
        self.assertEqual(s1_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s1_list.tail.next, None)    

    def test_find_all_in_empty_list(self):
        s_list = LinkedList()
        C = s_list.find_all(5)
        self.assertEqual(C, [])                # На выходе - пустой список

    def test_find_all_wrong(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5]
        s2_list = LinkedList()
        for i in list1:
            n = Node(i)
            s2_list.add_in_tail(n)
        C = s2_list.find_all(6)        
        self.assertEqual(C, [])                # На выходе - пустой список
        
    def test_clean(self):
        for i in range(1000):
            N = random.randint(0, 15)
            s3_list = LinkedList()
            for i in range(N):
                n = Node(random.randint(1, 9))
                s3_list.add_in_tail(n)
            s3_list.clean()
            self.assertEqual(s3_list.head, None)
            self.assertEqual(s3_list.tail, None)
 
    def test_len(self):
        for i in range(1000):
            N = random.randint(0, 20)
            s4_list = LinkedList()
            for i in range(N):
                n = Node(random.randint(1, 9))
                s4_list.add_in_tail(n)
            self.assertEqual(N, s4_list.len())

    def test_delete_5_False(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5, 5]
        s5_list = LinkedList()
        for i in list1:
            n = Node(i)
            s5_list.add_in_tail(n)
        L = s5_list.len()
        s5_list.delete(5, False)
        self.assertEqual(s5_list.len(), L - 1)         # проверка длины измененного списка
        self.assertEqual(s5_list.head.value, 8)        # Проверка указателя head
        self.assertEqual(s5_list.head.next.value, 35)   
        self.assertEqual(s5_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s5_list.tail.next, None)    
            
    def test_delete_5_True(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5, 5]
        s5_list = LinkedList()
        for i in list1:
            n = Node(i)
            s5_list.add_in_tail(n)
        L = s5_list.len()
        s5_list.delete(5, True)
        self.assertEqual(s5_list.len(), L - 5)         # проверка длины измененного списка
        self.assertEqual(s5_list.head.value, 8)        # Проверка указателя head
        self.assertEqual(s5_list.head.next.value, 35)   
        self.assertEqual(s5_list.tail.value, 2)        # Проверка указателя tail
        self.assertEqual(s5_list.tail.next, None)    

    def test_delete_5_alone_unit_True(self):
        s6_list = LinkedList()
        s6_list.add_in_tail(Node(5))
        s6_list.delete(5, True)
        # результат - пустой список
        self.assertEqual(s6_list.head, None)               
        self.assertEqual(s6_list.tail, None)

    def test_delete_5_alone_unit_False(self):
        s7_list = LinkedList()
        s7_list.add_in_tail(Node(5))
        s7_list.delete(5, False)
        # результат - пустой список
        self.assertEqual(s7_list.head, None)               
        self.assertEqual(s7_list.tail, None)
        
    def test_delete_666_empty_list(self):
        s8_list = LinkedList()
        s8_list.delete(666, False)
        # результат - пустой список
        self.assertEqual(s8_list.head, None)               
        self.assertEqual(s8_list.tail, None)      
        
    def test_inserting_666_at_the_top(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 5, 5]
        s_list = LinkedList()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        s_list.insert(None, 666)  
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 666)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 5)   
        self.assertEqual(s_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None)    

    def test_inserting_666_at_the_middle(self):
        list1 = [5, 8, 35, 2, 31, 5, 17, 5, 5]
        s_list = LinkedList()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        s_list.insert(5, 666)  
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 666)   
        self.assertEqual(s_list.tail.value, 5)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None) 

    def test_inserting_666_at_the_tail(self):
        list1 = [5, 8, 35, 2, 31, 5, 17]
        s_list = LinkedList()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        s_list.insert(17, 666)  
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 8)   
        self.assertEqual(s_list.tail.value, 666)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None) 
        
    def test_inserting_666_at_the_empty_list(self):
        s_list = LinkedList()
        L = s_list.len()
        s_list.insert(None, 666)  
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 666)        # Проверка указателя head
        self.assertEqual(s_list.head.next, None)   
        self.assertEqual(s_list.tail.value, 666)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None)         
        
    def test_inserting_666_at_the_alone_unit_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(15))
        L = s_list.len()
        s_list.insert(15, 666)  
        self.assertEqual(s_list.len(), L + 1)         # проверка длины измененного списка
        self.assertEqual(s_list.head.value, 15)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 666)   
        self.assertEqual(s_list.tail.value, 666)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None)                 
        
    def test_inserting_wrong(self):
        list1 = [5, 8, 35, 2, 31, 5, 17]
        s_list = LinkedList()
        for i in list1:
            n = Node(i)
            s_list.add_in_tail(n)
        L = s_list.len()
        s_list.insert(99, 666)  
        self.assertEqual(s_list.len(), L)         # проверка длины списка (не должна измениться)
        self.assertEqual(s_list.head.value, 5)        # Проверка указателя head
        self.assertEqual(s_list.head.next.value, 8)   
        self.assertEqual(s_list.tail.value, 17)        # Проверка указателя tail
        self.assertEqual(s_list.tail.next, None)                 
        
if __name__ == '__main__':
    unittest.main()
