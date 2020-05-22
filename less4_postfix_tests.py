import unittest

class MyTestCase(unittest.TestCase):    
    
    def test_1(self):
        C = '82+5*9+='
        C1 = C[::-1]
        S = Stack()
        for i in C1:
            S.push(i)
        self.assertEqual(postfix_math(S), 59.0)
        
    def test_without_equality_sign(self):
        C = '82+5*9+'
        C1 = C[::-1]
        S = Stack()
        for i in C1:
            S.push(i)
        self.assertEqual(postfix_math(S), 59.0)            

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
