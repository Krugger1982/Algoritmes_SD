import random
import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_enqueue_and_size (self):
        for i in range (500):
            Example = []
            Ex = Queue()
            self.assertEqual(0, Ex.size())
            for j in range(random.randint(0, 20)):
                X = random.randint(0, 100)
                Example.append(X)
            for k in range(len(Example)):
                Ex.enqueue(Example[k])                      # Формируем тестовую очередь на основе списка  Example
            self.assertEqual(len(Example), Ex.size())       # проверка соответствия длины очереди
            
            
    def test_dequeue (self):
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        Ex = Queue()
        for i in range(len(Example)):
            Ex.enqueue(Example[i])
        self.assertEqual(len(Example), Ex.size())
        for i in range(len(Example)):
            self.assertEqual(Example[i], Ex.dequeue())   

    def test_dequeue_empty_queue (self):
        Ex = Queue()
        self.assertEqual(None, Ex.dequeue())      

    def test_dequeue_queue_alone_unit (self):
        Ex = Queue()
        current = random.randint(0, 100)
        Ex.enqueue(current)
        self.assertEqual(1, Ex.size())
        self.assertEqual(current, Ex.dequeue()) 
        self.assertEqual(None, Ex.dequeue()) 
        self.assertEqual(0, Ex.size())
    
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
