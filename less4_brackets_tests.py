import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_brackets_correct(self):
        A = '(()(()))'
        self.assertTrue(Brackets(A))

    def test_brackets_correct_1(self):
        A = '()'
        self.assertTrue(Brackets(A))
        
    def test_brackets_not_correct(self):
        A = '())'
        self.assertFalse(Brackets(A))
        
    def test_brackets_not_correct1(self):
        A = '))((('
        self.assertFalse(Brackets(A))
            

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
