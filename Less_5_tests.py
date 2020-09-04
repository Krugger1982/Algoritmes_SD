import unittest

class MyTestCase(unittest.TestCase):
    def test_1(self):
        # создадим тестовый массив
        Test_List = [24, 14, 18, 8, 16, 31, 10, 22, 4, 28, 20, 12, 6, 2, 26]
        # И как он должен будет выглядеть в виде дерева поиска
        Keys = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 31]
        Test_result = GenerateBBSTArray(Test_List)
        for i in range (len(Test_result)):
            self.assertEqual(Test_result[i], Keys[i])
            
    def test_2(self):
        # создадим тестовый массив
        Test_List = [7, 5, 1, 4, 6, 2, 3]
        # И как он должен будет выглядеть в виде дерева поиска
        Keys = [4, 2, 6, 1, 3, 5, 7]
        Test_result = GenerateBBSTArray(Test_List)
        for i in range (len(Test_result)):
            self.assertEqual(Test_result[i], Keys[i])            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
