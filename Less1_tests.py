import unittest
import random

class MyTestCase(unittest.TestCase):    
    
    def test_1(self):
        print()
        print('Test clean')
        # Создадим длинный список размером 20 с рандомными элементами
        N = 20
        s_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s_list.add_in_tail(n)
        s_list.print_all_nodes()
        print()
        s_list.clean()
        print('Длина списка равна ', s_list.len())
        print()
        
    def test_2(self):
        print()
        print('Test delete 5')
        N = 30
        s_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(3, 7))
            s_list.add_in_tail(n)
        s_list.print_all_nodes()
        print()
        s_list.delete(5, False)
        print()
        s_list.print_all_nodes()   
        print() 
        print('Test delete 5 all')
        s_list.delete(5, True)
        s_list.print_all_nodes()
        print()
        print('Test delete 3 for alone unit')
        s1_list = LinkedList()
        s1_list.add_in_tail(Node(3))
        s1_list.print_all_nodes()
        print()        
        s1_list.delete(3, False)
        s1_list.print_all_nodes()
        print('Длина списка равна ', s1_list.len())
        print('Test delete 3 for empty list')
        s2_list = LinkedList()
        s2_list.delete(3, False)
        s2_list.print_all_nodes()
        print('Длина списка равна ', s2_list.len())

    def test_4(self):
        print()
        print('Test len')
        N = 20
        s_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s_list.add_in_tail(n)
        print('Заданный размер списка равен ', N)
        print('Посчитанный размер списка равен ', s_list.len())
        
    def test_5(self):
        print()
        print('Test find')
        N = 20
        s_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s_list.add_in_tail(n)
        s_list.print_all_nodes()
        print()
        print(s_list.find(5))
        print()
        print('Test find all 5')
        N = 20
        s_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s_list.add_in_tail(n)
        print()
        s_list.print_all_nodes()
        C = s_list.find_all(5)  
        print()
        print(C)


    def test_6(self):
        print()
        print('Test Вставка в начало')
        N = 20
        s_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s_list.add_in_tail(n)
        s_list.print_all_nodes()
        print()
        s_list.insert(None, 36)  
        s_list.print_all_nodes()
        print()
        print()
        print('Test Вставка после 5')
        s_list.insert(5, 36)  
        s_list.print_all_nodes()
        print()
        print()
        print('Test Вставка в пустой список')
        s_list.clean()  
        s_list.print_all_nodes()
        s_list.insert(None, 36)  
        print()
        s_list.print_all_nodes()
        
    def test_7(self):
        print()
        print('Test summa')
        N = 20
        s1_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s1_list.add_in_tail(n)
        s2_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s2_list.add_in_tail(n)
        s1_list.print_all_nodes()
        print()
        s2_list.print_all_nodes()
        print()
        s3_list = list_summa(s1_list, s2_list)
        print()
        s3_list.print_all_nodes()
        print()
        
if __name__ == '__main__':
    unittest.main()
