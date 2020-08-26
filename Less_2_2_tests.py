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
        self.assertEqual(Tree.Count(), 13)                          # проверка - всего 13 элементов
        Example1 = Tree.Root                                        # тестируем минимум/максимум всего дерева (слева и справа крайние листы отсутствуют)
        Example2 = Tree.FindNodeByKey(4).Node                       # тестируем поддерево слева неполное, а справа полное
        Example3 = Tree.FindNodeByKey(10).Node                      # тестируем полное поддерево
        self.assertEqual(Tree.FinMinMax(Example1, True).NodeKey, 14)
        self.assertEqual(Tree.FinMinMax(Example1, False).NodeKey, 2)
        self.assertEqual(Tree.FinMinMax(Example2, True).NodeKey, 7)
        self.assertEqual(Tree.FinMinMax(Example2, False).NodeKey, 2)
        self.assertEqual(Tree.FinMinMax(Example3, True).NodeKey, 11)
        self.assertEqual(Tree.FinMinMax(Example3, False).NodeKey, 9)
        
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
        self.assertTrue(Tree.DeleteNodeByKey(8))                   # Удаляем  единственный элемент
        self.assertEqual(Tree.Count(), 0)                          # Поверка - количество уменьшилось
        self.assertEqual(Tree.Root, None)                           # Проверка - дерево стало пустым
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
        self.assertTrue(Tree.DeleteNodeByKey(1))                    # Удаляем лист 1 (левый)
        self.assertEqual(Tree.Count(), 14)                          # Поверка - количество уменьшилось
        self.assertFalse(Tree.FindNodeByKey(1).NodeHasKey)          # Проверка - ключ 1 не найден
        self.assertEqual(Tree.FindNodeByKey(1).Node.NodeKey, 2)     # При поиске узла 1 найден его будущий родитель - узел 2
        self.assertTrue(Tree.FindNodeByKey(1).ToLeft)               # При поиске узла 1 найдено его будущее место - слева от узла 2
        
        self.assertTrue(Tree.DeleteNodeByKey(2))                    # Удаляем элемент 2 - (только 1 правый потомок)
        self.assertEqual(Tree.Count(), 13)                          # Поверка - количество уменьшилось
        self.assertFalse(Tree.FindNodeByKey(2).NodeHasKey)          # Проверка - ключ 2 не найден
        self.assertEqual(Tree.FindNodeByKey(2).Node.NodeKey, 3)     # При поиске узла 2 найден его будущий родитель - узел 3
        self.assertTrue(Tree.FindNodeByKey(2).ToLeft)               # При поиске узла 2 найдено его будущее место - слева от узла 3
        
        self.assertFalse(Tree.DeleteNodeByKey(2))                   # Повторно удалить элемент 2 не получится, вернется False
        self.assertEqual(Tree.Count(), 13)                          # Количество не изменилось
        
        self.assertTrue(Tree.DeleteNodeByKey(15))                   # Удаляем лист 15 (правый)
        self.assertEqual(Tree.Count(), 12)                          # Поверка - количество уменьшилось
        self.assertFalse(Tree.FindNodeByKey(1).NodeHasKey)          # Проверка - ключ 15 не найден
        self.assertEqual(Tree.FindNodeByKey(15).Node.NodeKey, 14)   # При поиске узла 15 найден его будущий родитель - узел 14
        self.assertFalse(Tree.FindNodeByKey(15).ToLeft)             # При поиске узла 15 найдено его будущее место - справа от узла 14
        
        self.assertTrue(Tree.DeleteNodeByKey(14))                   # Удаляем элемент 14 - (только 1 левый потомок)
        self.assertEqual(Tree.Count(), 11)                          # Поверка - количество уменьшилось
        self.assertFalse(Tree.FindNodeByKey(14).NodeHasKey)         # Проверка - ключ 14 не найден
        self.assertEqual(Tree.FindNodeByKey(14).Node.NodeKey, 13)   # При поиске узла 14 найден его будущий родитель - узел 13
        self.assertFalse(Tree.FindNodeByKey(14).ToLeft)             # При поиске узла 14 найдено его будущее место - справа от узла 13
        self.assertFalse(Tree.DeleteNodeByKey(14))                  # Повторно удалить элемент 14 не получится, вернется False
     
        self.assertTrue(Tree.DeleteNodeByKey(6))                                        # Удаляем узел 6 (два потомка). На его место встанет узел 7
        self.assertFalse(Tree.FindNodeByKey(6).NodeHasKey)                              # Проверка - ключ 6 не найден        
        self.assertEqual(Tree.Count(), 10)                                              # Количество уменьшилось
        self.assertEqual(Tree.FindNodeByKey(7).Node.RightChild, None)                   # теперь правый потомок узла 7 - это None   
        self.assertEqual(Tree.FindNodeByKey(7).Node.LeftChild.NodeValue, 'Echo')        # а левый потомок узла 7 - узел 5
        self.assertEqual(Tree.FindNodeByKey(5).Node.Parent.NodeKey, 7)                  # Сам узел 7 стал родителем узла 5



        self.assertTrue(Tree.DeleteNodeByKey(8))                                        # Удаляем корень. На его место встанет узел 9
        self.assertFalse(Tree.FindNodeByKey(8).NodeHasKey)                              # Проверка - ключ 8 не найден        
        self.assertEqual(Tree.Count(), 9)                                               # Количество уменьшилось
        self.assertEqual(Tree.FindNodeByKey(9).Node.RightChild.NodeValue, 'Lima')       # теперь правый потомок узла 9 - это узел 4
        self.assertEqual(Tree.FindNodeByKey(4).Node.Parent.NodeValue, 'India')          # а родитель узла 4 - узел 9
        self.assertEqual(Tree.FindNodeByKey(9).Node.LeftChild.NodeValue, 'Delta')       # левый потомок узла 9 - узел 12
        self.assertEqual(Tree.FindNodeByKey(12).Node.Parent.NodeValue, 'India')         # а родитель узла 12 - узел 9
        self.assertEqual(Tree.FindNodeByKey(10).Node.LeftChild, None)                   # Сам узел 9 удалился из детей узла 10
         
    
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
