import random
import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_insert_The_buffer_does_not_overflow(self):
        for j in range (500):
            n = random.randint(4, 9)
            N = (2 ** n) - 1                    # генерируем размер массива N меньший чем capacity
            A = DynArray()
            for i in range (N):
                X = random.randint(1, 50)
                A.append(X)                     # Формируем тестовый массив размера N
            target = random.randint(51, 100)    # обьект target заведомо не совпадающий с элементами массива А
            I = random.randint(0, N)
            A.insert(I, target)                 # Вставляем target в позицию I
            
            self.assertEqual(A.count, N + 1)        # проверка изменившегося размера массива
            self.assertEqual(A[I], target)          # проверка правильно вставленного target
            self.assertEqual(A.capacity, N + 1)     # проверка неизменившегося размера буфера
            
    def test_insert_the_buffer_is_full(self):
        for j in range (500):
            n = random.randint(4, 9)
            N = (2 ** n)                        # генерируем размер массива N равный  capacity
            A = DynArray()
            for i in range (N):
                X = random.randint(1, 50)
                A.append(X)                     # Формируем тестовый массив размера N
            target = random.randint(51, 100)    # обьект target заведомо не совпадающий с элементами массива А
            I = random.randint(0, N)
            A.insert(I, target)                 # Вставляем target в позицию I
            
            self.assertEqual(A.count, N + 1)        # проверка изменившегося размера массива
            self.assertEqual(A[I], target)          # проверка правильно вставленного target
            self.assertEqual(A.capacity, 2*N)       # проверка удвоения буфера
            
    def test_insert_wrong_index(self):
        """ Тест проверяет что всегда в случае задания неправильного индекса генерируется исключение и вставка не выполняется
        """
        for j in range (500):
            n = random.randint(4, 9)
            N = (2 ** n)- 1                        # генерируем размер массива N меньший чем capacity
            A = DynArray()
            for i in range (N):
                X = random.randint(1, 50)
                A.append(X)                             # Формируем тестовый массив размера N
            target = random.randint(51, 100)            # обьект target заведомо не совпадающий с элементами массива А            
            I_1 = random.randint(N + 1, N + 20)         # Генерируем идекс выходящий за размер массива вправо, то есть больший чемN
            I_2 = - random.randint(1, N + 20)           # Генерируем отрицательный индекс
            try:
                A.insert(I_1, target)                   # Пытаемся вставить target в позицию I_1
            except IndexError:
                pass        
            finally:
                self.assertEqual(A.count, N)            # проверка не изменившегося размера массива
            try:
                A.insert(I_2, target)                   # Пытаемся вставить target в позицию I_2
            except IndexError:
                pass        
            finally:
                self.assertEqual(A.count, N)            # проверка не изменившегося размера массива

    def test_delete_the_buffer_size_does_not_change(self):
        for j in range (500):
            n = random.randint(4, 10)
            N = (2 ** n) - 1                        # генерируем размер массива N меньший чем capacity на единицу(то есть заполненный более чем на половину)
            A = DynArray()
            for i in range (N):
                X = random.randint(1, 50)
                A.append(X)                         # Формируем тестовый массив размера N
            self.assertEqual(A.capacity, N + 1)     # проверка размера буфера            
            I = random.randint(0, N - 1)
            if I != N - 1:                          # если удаляемый элемент не последний
                Next = A[I + 1]                     # запоминаем следующий за ним элемент
                A.delete(I)
                self.assertEqual(A.count, N - 1)        # проверка изменившегося размера массива
                self.assertEqual(A[I], Next)            # проверка правильного смещения после удаления
                self.assertEqual(A.capacity, N + 1)     # проверка неизменившегося размера буфера
            else:                                       
                A.delete(I)
                self.assertEqual(A.count, N - 1)        # проверка изменившегося размера массива
                self.assertEqual(A.capacity, N + 1)     # проверка неизменившегося размера буфера                

    def test_delete_the_buffer_size_decreases(self):
        for j in range (500):
            n = random.randint(5, 10)
            N = 2 ** (n-1)                       # генерируем размер массива N равный половине буфера
            A = DynArray()
            for i in range (N + 1):              # Заполняем массив N+1 элементами, чтоб буфер увеличился
                X = random.randint(1, 50)
                A.append(X)                         # Формируем тестовый массив размера N + 1 
            self.assertEqual(A.capacity, 2 * N)     # проверка размера буфера
            A.delete(N)                             # Удаляем лишний элемент, теперь буфер заполнен ровно на половину
            I = random.randint(0, N - 1)
            if I != N - 1:                                      # если удаляемый элемент не последний
                Next = A[I + 1]                                 # запоминаем следующий за ним элемент
                A.delete(I)
                self.assertEqual(A.count, N - 1)                # проверка изменившегося размера массива
                self.assertEqual(A[I], Next)                    # проверка правильного смещения после удаления
                self.assertEqual(A.capacity, int(2*N / 1.5))    # проверка изменившегося размера буфера
            else:                                               
                A.delete(I)
                self.assertEqual(A.count, N - 1)                # проверка изменившегося размера массива
                self.assertEqual(A.capacity, int(2*N / 1.5))    # проверка изменившегося размера буфера

    def test_delete_the_buffer_size_is_reduced_to_less_than_minimum(self):
        """ Тест проверяет все случаи когда есть уменьшение буфера в 1.5 приведет к размеру  меньше минимального,
            и буфер должен принять размер 16
        """
        for j in range (16, 26):                    # проверяемый диапазон размеров буфера
            N = (j + 1) // 2                        # выберем размер массива N так, чтобы N-1 <= j/2 < N
            A = DynArray()
            for i in range (N):                     # Заполняем массив N элементами
                X = random.randint(1, 50)
                A.append(X)                         
            A.resize(j)                             # Задаем размер буфера равный j
            I = random.randint(0, N - 1)
            if I != N - 1:                                      # если удаляемый элемент не последний
                Next = A[I + 1]                                 # запоминаем следующий за ним элемент
                A.delete(I)
                self.assertEqual(A.count, N - 1)                # проверка изменившегося размера массива
                self.assertEqual(A[I], Next)                    # проверка правильного смещения после удаления
                self.assertEqual(A.capacity, 16)                # проверка размера буфера
            else:                                               
                A.delete(I)
                self.assertEqual(A.count, N - 1)                # проверка изменившегося размера массива
                self.assertEqual(A.capacity, 16)                # проверка размера буфера             

    def test_delete_wrong_index(self):
        """ Тест проверяет что всегда в случае задания неправильного индекса генерируется исключение и удаление не выполняется
        """
        for j in range (500):
            n = random.randint(4, 9)
            N = (2 ** n)- 1                        
            A = DynArray()
            for i in range (N):
                X = random.randint(1, 50)
                A.append(X)                             # Формируем тестовый массив размера N
            I_1 = random.randint(N + 1, N + 20)         # Генерируем идекс, больший чем N
            I_2 = - random.randint(1, N + 20)           # Генерируем отрицательный индекс
            try:
                A.delete(I_1)                           # Пытаемся удалить элемент из позиции I_1
            except IndexError:
                pass
            finally:
                self.assertEqual(A.count, N)
            try:
                A.delete(I_2)                           # Пытаемся удалить элемент из позиции I_2
            except IndexError:
                pass
            finally:
                self.assertEqual(A.count, N)
                
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
