import unittest

class MyTestCase(unittest.TestCase):
    def test_1_add(self):
        # создаем тестовое дерево глубиной в 4 уровня
        #                      0(8)
        #                   /       \
        #                 /           \
        #               /               \
        #           1(4)                  2(12)
        #          /     \               /       \
        #      3(2)      4(6)         5(10)       6(14) 
        #      / \       /   \        /   \      /     \ 
        #   7(1) 8(3)  9(5) 10(7) 11(9) 12(11) 13(13)  14(15)

        Tree = aBST(3)
        self.assertEqual(Tree.AddKey(8), 0)     # проверка - ключ 8 вставился в позицию 1
        self.assertEqual(Tree.AddKey(4), 1)
        self.assertEqual(Tree.AddKey(12), 2)
        self.assertEqual(Tree.AddKey(2), 3)
        self.assertEqual(Tree.AddKey(6), 4)
        self.assertEqual(Tree.AddKey(10), 5)
        self.assertEqual(Tree.AddKey(14), 6)
        self.assertEqual(Tree.AddKey(1), 7)
        self.assertEqual(Tree.AddKey(3), 8)
        self.assertEqual(Tree.AddKey(5), 9)
        self.assertEqual(Tree.AddKey(7), 10)     # левая половина дерева (все, что меньше 8) - заполнена
        self.assertEqual(Tree.AddKey(0), -1)       # поверка - ключ 0 не вставится - нет свободного места
        self.assertEqual(Tree.AddKey(9), 11)
        self.assertEqual(Tree.AddKey(11), 12)
        self.assertEqual(Tree.AddKey(13), 13)
        self.assertEqual(Tree.AddKey(15), 14)     # все дерево заполнено
        self.assertEqual(Tree.AddKey(19), -1)       # поверка - ключ 19 не вставится - нет свободного места
        
    def test_2_add_and_find(self):
        # создаем тестовое дерево глубиной в 4 уровня
        #                      0(16)
        #                   /       \
        #                 /           \
        #               /               \
        #           1(8)                  2(24)
        #          /     \               /       \
        #      3(4)      4(12)         5(20)       6(28) 
        #      / \       /   \        /   \      /     \ 
        #   7(2) 8(6) 9(10) 10(14) 11(18) 12(22) 13(26)  14(31)

        Test_Tree = aBST(3)
        Test_Tree.AddKey(16)
        Test_Tree.AddKey(8)
        Test_Tree.AddKey(24)
        Test_Tree.AddKey(4)
        Test_Tree.AddKey(12)
        Test_Tree.AddKey(20)
        Test_Tree.AddKey(28)
        Test_Tree.AddKey(2)
        Test_Tree.AddKey(6)
        Test_Tree.AddKey(10)
        Test_Tree.AddKey(14)      # левая половина дерева (все, что меньше 16) - заполнена
        self.assertEqual(Test_Tree.AddKey(1), -1)       # поверка - ключ 1 не вставится - нет свободного места
        Test_Tree.AddKey(18)
        self.assertEqual( Test_Tree.FindKeyIndex(22), -3)          # проверка - ключа 22 еще нет, его место - индекс[-3] (то есть  индекс [12])
        Test_Tree.AddKey(22)
        Test_Tree.AddKey(26)
        Test_Tree.AddKey(31)     # все дерево заполнено
        # создадим тестовый массив ключей для проверки - так должен выглядеть массив проверяемого дерева
        Keys = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 31]
        for i in range(len(Keys)):
            self.assertEqual(Test_Tree.FindKeyIndex(Keys[i]), i)         # проверка - индексы тестового масссива и в массиве проверяемого дерева совпадают
        for i in range(len(Keys)):
            self.assertEqual(Keys[i], Test_Tree.Tree[i])                 # проверка - элементы массивов совпадают
            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
