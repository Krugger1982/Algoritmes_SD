import unittest

class MyTestCase(unittest.TestCase):

    def test_add_and_isValue (self):
        Test_Filter = BloomFilter(32)
        A = '0123456789'
        for i in range(len(A)):
            B = list(A)
            B.append(B[0])
            del B[0]                           
            A = ''.join(B)
            Test_Filter.add(A)
            self.assertTrue(Test_Filter.is_value(A))
            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
