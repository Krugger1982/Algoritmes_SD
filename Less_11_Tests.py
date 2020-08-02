import unittest
import random

class MyTestCase(unittest.TestCase):

    def test_1_put_and_size (self):
        # создаем тестовое множество из нескольких тысяч последовательных (неповторяющихся) чисел
        Set1 = PowerSet()
        N = 100000
        for i in range(N):
            Set1.put(i)
        self.assertEqual(N, Set1.size())    # проверка что мощность множества равна N
        for i in range(N//10):               # Снова добавляем чисел (чтоб повторялись)
            Set1.put(i)
        self.assertEqual(N, Set1.size())    # проверка что мощность множества снова равна N и не изменилась

    def test_2_remove(self):
        # создаем тестовое множество из последовательных (неповторяющихся) чисел
        Set1 = PowerSet()
        N = 35000
        M = N//2
        for i in range(N):
            Set1.put(i)
        for i in range(M):                  # Удаляем половину чисел
            self.assertTrue(Set1.remove(i)) # проверяем успешность каждого удаления
        self.assertEqual(N - M, Set1.size())    # размер множества стал N-M
        for i in range(M):                  # Удаляем половину чисел еще раз
            self.assertFalse(Set1.remove(i)) # проверяем неуспешность каждого удаления
        self.assertEqual(N - M, Set1.size()) # размер множества не изменился

    def test_3_intersection(self):
        # создаем тестовое множество из последовательных (неповторяющихся) чисел от 0 до N-1
        Set1 = PowerSet()
        # создаем второe множество 
        Set2 = PowerSet()
        N = 100
        M = 9
        for i in range(N):
            Set1.put(i)
        for i in range(M, M+N):
            Set2.put(i)                     # Второе множество наполняем числами от  M до N + M, то есть от 70 до 169
        Set3 = Set1.intersection(Set2)
        self.assertEqual(Set3.size(), N - M)    # Проверка по размеру множества (равно N-M) 
        for i in range (M, N):
            self.assertTrue(Set3.get(i))        # Проверка по содержимому (содержит числа от М до N)
        
    def test_4_union(self):
        Set1 = PowerSet()
        Set2 = PowerSet()
        N = 10000
        M = 5000
        for i in range(N):
            Set1.put(i)
        for i in range(M, M+N, 1):
            Set2.put(i)
        Set3 = Set1.union(Set2)
        self.assertEqual(Set3.size(), N + M)    # Проверка по размеру множества
        for i in range (M+N):
            self.assertTrue(Set3.get(i))        # Проверка по содержимому (содержит числа от 0 до N + M)

    def test_4_1_union_with_empty(self):
        Set1 = PowerSet()
        Set2 = PowerSet()
        N = 100
        for i in range(N):
            Set1.put(i)
        Set3 = Set1.union(Set2)
        self.assertEqual(Set3.size(), N)        # Проверка по размеру множества (не изменилось)

    def test_5_difference(self):
        # создаем тестовое множество из последовательных (неповторяющихся) чисел от 0 до N-1
        Set1 = PowerSet()
        # создаем второe множество 
        Set2 = PowerSet()
        N = 100
        M = 70
        for i in range(N):
            Set1.put(i)
        for i in range(M, M+N, 1):
            Set2.put(i)                     # Второе множество наполняем числами от  M до N + M, то есть от 70 до 169
        Set3 = Set1.difference(Set2)
        self.assertEqual(Set3.size(), M)    # Проверка по размеру множества (равно 70) 
        for i in range (M):
            self.assertTrue(Set3.get(i))        # Проверка по содержимому (содержит числа от 0 до M)

    def test_5_1_difference_Equal_Sets(self):
        # создаем тестовое множество из последовательных (неповторяющихся) чисел от 0 до N-1
        Set1 = PowerSet()
        # создаем второe множество 
        Set2 = PowerSet()
        N = 100
        M = 100
        for i in range(N):
            Set1.put(i)
        for i in range(M):
            Set2.put(i)                     # Второе множество наполняем числами от  M до N + M, то есть от 70 до 169
        Set3 = Set1.difference(Set2)
        self.assertEqual(Set3.size(), 0)    # Проверка по размеру множества (пустое) 

            
    def test_6_1_issubset(self):
        # создаем тестовое множество из последовательных (неповторяющихся) чисел от 0 до N-1
        Set1 = PowerSet()
        # создаем второe множество 
        Set2 = PowerSet()
        N = 100
        M = 70
        for i in range(N):
            Set1.put(i)
        for i in range(M):
            Set2.put(i)                     # Второе множество наполняем числами от  0 до  M,
        self.assertTrue(Set1.issubset(Set2))

    def test_6_2_issubset_Equal_Sets(self):
        # создаем тестовое множество из последовательных (неповторяющихся) чисел от 0 до N-1
        Set1 = PowerSet()
        # создаем второe множество 
        Set2 = PowerSet()
        N = 100
        M = 100
        for i in range(N):
            Set1.put(i)
        for i in range(M):
            Set2.put(i)                     # Второе множество идентично первому,
        self.assertTrue(Set1.issubset(Set2))

    def test_6_3_issubset_wrong(self):
        # создаем тестовое множество из последовательных (неповторяющихся) чисел от 0 до N-1
        Set1 = PowerSet()
        # создаем второe множество 
        Set2 = PowerSet()
        N = 70
        M = 100
        for i in range(N):
            Set1.put(i)
        for i in range(M):
            Set2.put(i)                     # Второе множество содержит в себе первое
        self.assertFalse(Set1.issubset(Set2))

    def test_6_4_issubset_wrong(self):
        # создаем тестовое множество из последовательных (неповторяющихся) чисел от 0 до N-1
        Set1 = PowerSet()
        # создаем второe множество 
        Set2 = PowerSet()
        N = 70
        M = 100
        for i in range(N):
            Set1.put(i)
        for i in range(N//2, M):
            Set2.put(i)                     # Второе мнодество состоит из чисел другого диапазона
        self.assertFalse(Set1.issubset(Set2))   # Результат - ложь
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
