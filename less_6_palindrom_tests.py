import unittest

class MyTestCase(unittest.TestCase):    
    def test_true(self):
        Ex = 'А Роза упала на лапу Азора'
        self.assertTrue(palindrom(Ex))
  
    def test_false(self):
        Ex = 'А Роза упала на лапу Буратино'
        self.assertFalse(palindrom(Ex))     
    
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
