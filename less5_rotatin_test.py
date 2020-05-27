import random
import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_1_rotqtion_zero (self):
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        Ex = Queue()
        for j in range(1000):                                             # 1000 прогонов
            Ex = Queue()
            for i in range(len(Example)):
                Ex.enqueue(Example[i])                                    # Формируем тестовую очередь из списка
            self.assertEqual(len(Example), Ex.size())
            i = random.randint(0, 100)
            A = rotation(Ex, i)                                           # вращаем очередь на рандомное число
            self.assertEqual(Example[i % len(Example)], A.dequeue())      # проверка, что оказалось в голове очереди
    
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
