import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_1(self):
        C1 = '82+5*5+5/10-='
        self.assertEqual(postfix_math(C1), 1.0)
        
    def test_without_equality_sign(self):
        C1 = '82+5*5+5/10-'
        self.assertEqual(postfix_math(C1), 1)            

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
