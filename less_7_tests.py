import unittest

class MyTestCase(unittest.TestCase):

    def test_add_ascending(self):
        list1 = [1, 8, 35, 2, 35, 31, 1, 8, 17, 10, 7]
        list_sorted = [1, 1, 2, 7, 8, 8, 10, 17, 31, 35, 35]
        Example = OrderedList(True)
        for i in list1:
            Example.add(i)
        current = Example.head
        self.assertEqual(list_sorted[0], current.value)
        current = current.next   
        self.assertEqual(list_sorted[1], current.value)
        current = current.next
        self.assertEqual(list_sorted[2], current.value)
        current = current.next   
        self.assertEqual(list_sorted[3], current.value)
        current = current.next   
        self.assertEqual(list_sorted[4], current.value)
        current = current.next   
        self.assertEqual(list_sorted[5], current.value)
        current = current.next   
        self.assertEqual(list_sorted[6], current.value)
        current = current.next   
        self.assertEqual(list_sorted[7], current.value)
        current = current.next
        self.assertEqual(list_sorted[8], current.value)
        current = current.next
        self.assertEqual(list_sorted[9], current.value)
        current = current.next   
        self.assertEqual(list_sorted[10], current.value)

    def test_add_descending(self):
        list1 = [1, 8, 35, 2, 35, 31, 1, 8, 17, 10, 7]
        list_sorted = [35, 35, 31, 17, 10, 8, 8, 7, 2, 1, 1]
        Example = OrderedList(False)
        for i in list1:
            Example.add(i)
        current = Example.head
        self.assertEqual(list_sorted[0], current.value)
        current = current.next   
        self.assertEqual(list_sorted[1], current.value)
        current = current.next
        self.assertEqual(list_sorted[2], current.value)
        current = current.next   
        self.assertEqual(list_sorted[3], current.value)
        current = current.next   
        self.assertEqual(list_sorted[4], current.value)
        current = current.next   
        self.assertEqual(list_sorted[5], current.value)
        current = current.next   
        self.assertEqual(list_sorted[6], current.value)
        current = current.next   
        self.assertEqual(list_sorted[7], current.value)
        current = current.next
        self.assertEqual(list_sorted[8], current.value)
        current = current.next
        self.assertEqual(list_sorted[9], current.value)
        current = current.next   
        self.assertEqual(list_sorted[10], current.value)

    def test_clean(self):
        list1 = [1, 8, 35, 2, 35, 31, 1, 8, 17, 10, 7]
        list_sorted = [1, 1, 2, 7, 8, 8, 10, 17, 31, 35, 35]
        Example = OrderedList(False)
        for i in list1:
            Example.add(i)
        Example.clean(True)
        self.assertEqual(0, Example.len())
        self.assertEqual(None, Example.head)
        self.assertEqual(None, Example.tail)

    def test_del_ascending(self):
        list1 = [1, 8, 35, 2, 35, 31, 1, 8, 17, 10, 7]
        list_sorted = [1, 1, 2, 7, 8, 8, 10, 17, 31, 35, 35]
        Example = OrderedList(True)
        for i in list1:
            Example.add(i)
        C = Example.find(10)
        L = Example.len()
        self.assertNotEqual(None, C)            # проверка что элемент С есть в списке
        Example.delete(10)
        C1 = Example.find(10)
        L1 = Example.len()
        self.assertEqual(None, C1)              # проверка что элемент С исчез из списка
        self.assertEqual(L-1, L1)               # проверка что изменился размер списка
        C2 = Example.find(17)               
        self.assertEqual(C2.prev.value, 8)      # проверка изменения связей у следующего и предыдущего элементов
    
    def test_del_descending(self):
        list1 = [1, 8, 35, 2, 35, 31, 1, 8, 17, 10, 7]
        list_sorted = [35, 35, 31, 17, 10, 8, 8, 7, 2, 1, 1]
        Example = OrderedList(False)
        for i in list1:
            Example.add(i)
        C = Example.find(10)
        L = Example.len()
        self.assertNotEqual(None, C)            # проверка что элемент С есть в списке
        Example.delete(10)
        C1 = Example.find(10)
        L1 = Example.len()
        self.assertEqual(None, C1)              # проверка что элемент С исчез из списка
        self.assertEqual(L-1, L1)               # проверка что изменился размер списка
        C2 = Example.find(8)
        self.assertEqual(C2.prev.value, 17)     # проверка изменения связей у следующего и предыдущего элементов
        
    def test_find_ascending(self):
        list1 = [1, 8, 35, 2, 31, 8, 17, 10, 7]
        list_sorted = [1, 2, 7, 8, 8, 10, 17, 31, 35]
        Example = OrderedList(True)
        for i in list1:
            Example.add(i)
        C = Example.find(8)
        self.assertEqual (C.value, 8)           # Проверка элемента - поле value 
        self.assertEqual(C.next.value, 8)       # Проверка  поля next
        self.assertEqual(C.prev.value, 7)       # Проверка  поля prev
        C = Example.find(35)
        self.assertEqual (C.value, 35)          # Проверка элемента - поле value 
        self.assertEqual(C.next, None)          # Проверка  поля next
        self.assertEqual(C.prev.value, 31)      # Проверка  поля prev
        self.assertEqual(Example.head.value, 1)        # Проверка указателя head
        self.assertEqual(Example.head.next.value, 2)
        self.assertEqual(Example.head.prev, None)
        self.assertEqual(Example.tail.value, 35)        # Проверка указателя tail
        self.assertEqual(Example.tail.prev.value, 31)
        self.assertEqual(Example.tail.next, None)
        C = Example.find(3)                             # поиск несуществующего значения
        self.assertEqual(C, None)

    def test_find_descending(self):
        list1 = [1, 8, 35, 2, 31, 8, 17, 10, 7]
        list_sorted = [35, 31, 17, 10, 8, 8, 7, 2, 1]
        Example = OrderedList(False)
        for i in list1:
            Example.add(i)
        C = Example.find(8)
        self.assertEqual (C.value, 8)           # Проверка элемента - поле value 
        self.assertEqual(C.next.value, 8)       # Проверка  поля next
        self.assertEqual(C.prev.value, 10)       # Проверка  поля prev
        C = Example.find(35)
        self.assertEqual (C.value, 35)          # Проверка элемента - поле value 
        self.assertEqual(C.prev, None)          # Проверка  поля prev
        self.assertEqual(C.next.value, 31)      # Проверка  поля next
        self.assertEqual(Example.head.value, 35)        # Проверка указателя head
        self.assertEqual(Example.head.next.value, 31)
        self.assertEqual(Example.head.prev, None)
        self.assertEqual(Example.tail.value, 1)         # Проверка указателя tail
        self.assertEqual(Example.tail.prev.value, 2)
        self.assertEqual(Example.tail.next, None)
        C = Example.find(3)                             # поиск несуществующего значения
        self.assertEqual(C, None)

    def test_len (self):
        list1 = [1, 8, 35, 2, 35, 31, 1, 8, 17, 10, 7]
        list_sorted = [1, 1, 2, 7, 8, 8, 10, 17, 31, 35, 35]
        Example = OrderedList(True)
        for i in list1:
            Example.add(i)
        self.assertEqual(len(list1), Example.len())

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
