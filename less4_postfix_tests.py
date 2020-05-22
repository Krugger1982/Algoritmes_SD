import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_1(self):
        C1 = '8 2 + 5 * 5 + 5 / 10 - ='
        self.assertEqual(postfix_math(C1), 1.0)
        
    def test_without_equality_sign(self):
        C1 = '8 2 + 5 * 5 + 5 / 10 -'
        self.assertEqual(postfix_math(C1), 1)            

    def test_division(self):
        C1 = '5 5 55 + 5 / ='
        self.assertEqual(postfix_math(C1), 13)

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
