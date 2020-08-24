import unittest

class MyTestCase(unittest.TestCase):
    def test_1_empty_tree(self):
        Tree = BST(None)
        Tree.AddKeyValue(8, 'Hotel')
        self.assertEqual(Tree.Count(), 1)
        self.assertFalse(Tree.FindNodeByKey(5).NodeHasKey)  # Проверка - ключ 5 не найден

    
    def test_2_add_and_Find_and_Count (self):
        # создаем тестовое дерево
        #       Root         H(8)
        #               /           \
        #           D(4)            L(12)
        #          /     \           /    \
        #      B(2)      F(6)      J(10)   N(14) 
        #      / \       /   \     / \        /   \ 
        #   A(1) C(3)  E(5) G(7) I(9) K(11) M(13) O(15)

        Tree = BST(None)
        self.assertTrue(Tree.AddKeyValue(8, 'Hotel'))
        self.assertTrue(Tree.AddKeyValue(4, 'Delta'))
        Tree.AddKeyValue(12, 'Lima')
        Tree.AddKeyValue(2, 'Bravo')
        Tree.AddKeyValue(6, 'Foxtrot')
        Tree.AddKeyValue(10, 'Juliet')
        Tree.AddKeyValue(14, 'November')
        Tree.AddKeyValue(1, 'Alfa')
        Tree.AddKeyValue(3, 'Charlie')
        Tree.AddKeyValue(5, 'Echo')
        Tree.AddKeyValue(7, 'Golf')
        Tree.AddKeyValue(9, 'India')
        Tree.AddKeyValue(11, 'Kilo')
        Tree.AddKeyValue(13, 'Mike')
        Tree.AddKeyValue(15, 'Oscar')
        self.assertEqual(Tree.Count(), 15)
        self.assertFalse(Tree.AddKeyValue(15, 'Oscar2'))                    # попробуем добавить уже существующий ключ, вернется False
        self.assertEqual(Tree.Count(), 15)                                  # проверка - количество не изменилось
        self.assertEqual(Tree.FindNodeByKey(15).Node.NodeValue, 'Oscar')    # Проверка - остался узел "Oscar",  а не "Oscar2"
        self.assertEqual(Tree.FindNodeByKey(5).Node.Parent.NodeKey, 6)      # Правильно записался лист 5, его родитель - узел 6 "Foxtrot"
        self.assertEqual(Tree.FindNodeByKey(5).Node.NodeValue, 'Echo')      # А его содержимое - 'Echo'
        self.assertEqual(Tree.FindNodeByKey(2).Node.Parent.NodeKey, 4)      # Правильно записался лист 2, его родитель - узел 4 "Delta"
        self.assertEqual(Tree.FindNodeByKey(2).Node.LeftChild.NodeKey, 1)
        self.assertEqual(Tree.FindNodeByKey(2).Node.RightChild.NodeKey, 3)  # А дети - узлы 1 и 3

    def test_3_add_and_Find_and_Count (self):
        # создаем тестовое дерево
        #       Root         H(8)
        #               /             \
        #           D(4)              L(12)
        #          /     \           /     \
        #      B(2)      F(6)      J(10)    N(14) 
        #      / \         \       /         /   \ 
        #   A(1) C(3)      G(7)  I(9)      M(13) O(15)

        Tree = BST(None)
        Tree.AddKeyValue(8, 'Hotel')
        Tree.AddKeyValue(4, 'Delta')
        Tree.AddKeyValue(12, 'Lima')
        Tree.AddKeyValue(2, 'Bravo')
        Tree.AddKeyValue(6, 'Foxtrot')
        Tree.AddKeyValue(10, 'Juliet')
        Tree.AddKeyValue(14, 'November')
        Tree.AddKeyValue(1, 'Alfa')
        Tree.AddKeyValue(3, 'Charlie')
                                        # Лист 5 отсутствует
        Tree.AddKeyValue(7, 'Golf')
        Tree.AddKeyValue(9, 'India')
                                        # Лист 11 отсутствует
        Tree.AddKeyValue(13, 'Mike')
        Tree.AddKeyValue(15, 'Oscar')
        self.assertEqual(Tree.Count(), 13)                                      # Проверка - записались 13 узлов
        self.assertEqual(Tree.FindNodeByKey(14).Node.NodeValue, 'November')     # Проверка - в узле 14 хранится "November"
        self.assertTrue(Tree.FindNodeByKey(14).NodeHasKey)                      # Проверка - ключ найден
        self.assertFalse(Tree.FindNodeByKey(5).NodeHasKey)          # Проверка - ключ 5 не найден
        self.assertEqual(Tree.FindNodeByKey(5).Node.NodeKey, 6)     # При поиске узла 5 найден его будущий родитель - узел 6
        self.assertTrue(Tree.FindNodeByKey(5).ToLeft)               # При поиске узла 5 найдено его будущее место - слева от узла 6
        self.assertFalse(Tree.FindNodeByKey(11).NodeHasKey)         # Проверка - ключ 11 не найден
        self.assertEqual(Tree.FindNodeByKey(11).Node.NodeKey, 10)   # При поиске узла 11 найден его будущий родитель - узел 10
        self.assertFalse(Tree.FindNodeByKey(11).ToLeft)             # При поиске узла 11 найдено его будущее место - справа от узла 10

    def test_4_FindMinMax (self):
        # создаем тестовое дерево
        #
        #       Root          H(8)
        #                 /        \
        #               /             \
        #           D(4)                L(12)
        #          /    \              /      \
        #      B(2)      F(6)       J(10)     N(14) 
        #        \      /   \       / \        /     
        #        C(3)  E(5) G(7) I(9) K(11)  M(13)  

        Tree = BST(None)
        Tree.AddKeyValue(8, 'Hotel')
        Tree.AddKeyValue(4, 'Delta')
        Tree.AddKeyValue(12, 'Lima')
        Tree.AddKeyValue(2, 'Bravo')
        Tree.AddKeyValue(6, 'Foxtrot')
        Tree.AddKeyValue(10, 'Juliet')
        Tree.AddKeyValue(14, 'November')
                                                # Пусть отсутствует элемент 1
        Tree.AddKeyValue(3, 'Charlie')
        Tree.AddKeyValue(5, 'Echo')
        Tree.AddKeyValue(7, 'Golf')
        Tree.AddKeyValue(9, 'India')
        Tree.AddKeyValue(11, 'Kilo')
        Tree.AddKeyValue(13, 'Mike')
                                                # и пусть отсутствует элемент 15
        self.assertEqual(Tree.Count(), 13)      # проверка - всего 13 элементов
        Example1 = Tree.Root                    # проверяем минимум/максимум всего дерева (слева и справа крайние листы отсутствуют)
        Example2 = Tree.FindNodeByKey(4).Node   # поддерево слева неполное, а справа полное
        Example3 = Tree.FindNodeByKey(10).Node  # полное поддерево
        self.assertEqual(Tree.FinMinMax(Example1, True), 14)
        self.assertEqual(Tree.FinMinMax(Example1, False), 2)
        self.assertEqual(Tree.FinMinMax(Example2, True), 7)
        self.assertEqual(Tree.FinMinMax(Example2, False), 2)
        self.assertEqual(Tree.FinMinMax(Example3, True), 11)
        self.assertEqual(Tree.FinMinMax(Example3, False), 9)
        
    def test_5_delete (self):
        # создаем тестовое дерево
        #       Root         H(8)
        #               /           \
        #           D(4)            L(12)
        #          /     \           /    \
        #      B(2)      F(6)      J(10)   N(14) 
        #      / \       /   \     / \        /   \ 
        #   A(1) C(3)  E(5) G(7) I(9) K(11) M(13) O(15)

        Tree = BST(None)
        Tree.AddKeyValue(8, 'Hotel')
        Tree.AddKeyValue(4, 'Delta')
        Tree.AddKeyValue(12, 'Lima')
        Tree.AddKeyValue(2, 'Bravo')
        Tree.AddKeyValue(6, 'Foxtrot')
        Tree.AddKeyValue(10, 'Juliet')
        Tree.AddKeyValue(14, 'November')
        Tree.AddKeyValue(1, 'Alfa')
        Tree.AddKeyValue(3, 'Charlie')
        Tree.AddKeyValue(5, 'Echo')
        Tree.AddKeyValue(7, 'Golf')
        Tree.AddKeyValue(9, 'India')
        Tree.AddKeyValue(11, 'Kilo')
        Tree.AddKeyValue(13, 'Mike')
        Tree.AddKeyValue(15, 'Oscar')
        self.assertTrue(Tree.FindNodeByKey(1).NodeHasKey)           # проверка - ключ 1 присутствует   
        Tree.DeleteNodeByKey(1)                                     # Удаляем лист 1
        self.assertEqual(Tree.Count(), 14)                          # Поверка - количество уменьшилось
        self.assertFalse(Tree.FindNodeByKey(1).NodeHasKey)          # Проверка - ключ 1 не найден
        self.assertEqual(Tree.FindNodeByKey(1).Node.NodeKey, 2)     # При поиске узла 1 найден его будущий родитель - узел 2
        self.assertTrue(Tree.FindNodeByKey(1).ToLeft)               # При поиске узла 1 найдено его будущее место - слева от узла 2
        Tree.DeleteNodeByKey(2)                                     # Удаляем элемент 2 - уже с 1-м потомком
        self.assertEqual(Tree.Count(), 13)                          # Поверка - количество уменьшилось
        self.assertFalse(Tree.FindNodeByKey(2).NodeHasKey)          # Проверка - ключ 2 не найден
        self.assertEqual(Tree.FindNodeByKey(2).Node.NodeKey, 3)     # При поиске узла 2 найден его будущий родитель - узел 3
        self.assertTrue(Tree.FindNodeByKey(2).ToLeft)               # При поиске узла 2 найдено его будущее место - слева от узла 3
        self.assertFalse(Tree.DeleteNodeByKey(2))                   # Повторно удалить элемент 2 не получится, вернется False
        self.assertEqual(Tree.Count(), 13)                          # Количество не изменилось 
        self.assertTrue(Tree.DeleteNodeByKey(8))                                        # Удаляем корень. На его место встанет узел 9
        self.assertEqual(Tree.FindNodeByKey(9).Node.RightChild.NodeValue, 'Lima')       # теперь правый потомок узла 9 - это узел 4   
        self.assertEqual(Tree.FindNodeByKey(9).Node.LeftChild.NodeValue, 'Delta')       # а левый потомок узла 9 - узел 12
        self.assertEqual(Tree.FindNodeByKey(10).Node.LeftChild, None)                   # Сам узел 9 удалился из детей узла 10
        
    
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
