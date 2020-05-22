import random
import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_push_and_size (self):
        for i in range (500):
            Example = []
            Ex = Stack()
            for i in range(random.randint(0, 20)):
                X = random.randint(0, 100)
                Example.append(X)
            for i in range(len(Example)):
                Ex.push(Example[i])             # Формируем тестовый стек на основе списка  Example
            self.assertEqual(len(Example), Ex.size())
            
    def test_peek_and_push (self):
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        Ex = Stack()
        for i in range(-1, -len(Example), -1):
            Ex.push(Example[i])
            self.assertEqual(Example[i], Ex.peek())
        
    def test_push_and_peek (self):
        S = Stack()
        for i in range (500):
            X = random.randint(1, 50)
            S.push(X)                             
            self.assertEqual(S.peek(), X)

    def test_push_and_pop (self):
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        Ex = Stack()
        for i in range(len(Example)):
            Ex.push(Example[i])
        for i in range(-1, -len(Example), -1):
            self.assertEqual(Example[i], Ex.pop())      

    def pop_empty_stack (self):
        Ex = Stack()
        self.assertEqual(None, Ex.pop())   
