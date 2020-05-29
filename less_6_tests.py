import random
import unittest

class MyTestCase(unittest.TestCase):    
    def test_size(self):
        Ex = Deque()
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        for i in Example:
            Ex.addFront(i)
        self.assertEqual(Ex.size(), 12)
    
    def test_addFront_removeFront_1(self):
        Ex = Deque()
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        for i in Example:
            Ex.addFront(i)
        self.assertEqual(Ex.size(), len(Example))
        for j in reversed(Example):
            self.assertEqual(Ex.removeFront(), j)

    def test_addFront_removeFront_2(self):
        Ex = Deque()
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        for i in Example:
            Ex.addFront(i)
        self.assertEqual(Ex.size(), len(Example))
        Ex.addFront('Proverka')
        self.assertEqual(Ex.size(), 13)
        self.assertEqual(Ex.removeFront(), 'Proverka')
            
    def test_addFront_removeFront(self):
        Ex = Deque()
        for i in range(1000):
            Example = []
            for j in range(random.randint(1, 50)):
                X = random.randint(1, 99)
                Example.append(X)
                Ex.addFront(X)
            self.assertEqual(Ex.size(), len(Example))
            for j in reversed(Example):
                self.assertEqual(Ex.removeFront(), j)

                
    def test_addTail_removeTail_1 (self):
        Ex = Deque()
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        for i in Example:
            Ex.addTail(i)
        self.assertEqual(Ex.size(), len(Example))
        for j in Example:
            self.assertEqual(Ex.removeFront(), j)

    def test_addFront_removeTail_2(self):
        Ex = Deque()
        Example = [5, 17, 69, 36, 2, 0, 16, 10, 99, 38, 15, 'fourteen']
        for i in Example:
            Ex.addFront(i)
        self.assertEqual(Ex.size(), len(Example))
        Ex.addTail('Proverka')
        self.assertEqual(Ex.size(), 13)
        self.assertEqual(Ex.removeTail(), 'Proverka')

    def test_addTail_removeTail(self):
        Ex = Deque()
        for i in range(1000):
            Example = []
            for j in range(random.randint(1, 50)):
                X = random.randint(1, 99)
                Example.append(X)
                Ex.addTail(X)
            self.assertEqual(Ex.size(), len(Example))
            for j in Example:
                self.assertEqual(Ex.removeFront(), j)        
    
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
