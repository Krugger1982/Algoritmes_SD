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

        Tree = aBST(4)
        Tree.AddKey(8)
        Tree.AddKey(4)
        Tree.AddKey(12)
        Tree.AddKey(2)
        Tree.AddKey(6)
        Tree.AddKey(10)
        Tree.AddKey(14)
        Tree.AddKey(1)
        Tree.AddKey(3)
        Tree.AddKey(5)
        Tree.AddKey(7)      # левая половина дерева (все, что меньше 8) - заполнена
        self.assertEqual(Tree.AddKey(0), -1)       # поверка - ключ 0 не вставится - нет свободного места
        Tree.AddKey(9)
        Tree.AddKey(11)
        Tree.AddKey(13)
        Tree.AddKey(15)     # все дерево заполнено
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

        Test_Tree = aBST(4)
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
