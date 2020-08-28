import unittest
         
    def test_6_DeepAllNodes (self):
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

        # И создадим тестовые массивы с ключами для поиска в глубину
        Array_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]       #   in-order
        Array_1 = [1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8]       #   post-order
        Array_2 = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]       #   pre-order
        res0 = Tree.DeepAllNodes(0)
        for i in range (len(res0)):
            self.assertEqual(res0[i].NodeKey, Array_0[i])
        res1 = Tree.DeepAllNodes(1)
        for i in range (len(res1)):
            self.assertEqual(res1[i].NodeKey, Array_1[i])
        res2 = Tree.DeepAllNodes(2)
        for i in range (len(res2)):
            self.assertEqual(res2[i].NodeKey, Array_2[i])

    def test_7_WideAllNodes (self):
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

        # И создадим тестовый массив с ключами для поиска в ширину
        Array_Wide_1 = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]       
        res = Tree.WideAllNodes()
        for i in range (len(res)):                              
            self.assertEqual(res[i].NodeKey, Array_Wide_1[i])     # проверка результата

        self.assertTrue(Tree.DeleteNodeByKey(1))                # Удаляем левый лист 
        Array_Wide_2 = [8, 4, 12, 2, 6, 10, 14, 3, 5, 7, 9, 11, 13, 15] # теперь тестовый массив будет выгляеть так       
        res = Tree.WideAllNodes()
        for i in range (len(res)):                              
            self.assertEqual(res[i].NodeKey, Array_Wide_2[i])     # проверка результата        

        self.assertTrue(Tree.DeleteNodeByKey(9))                # Удалим всю ветку J(10) 
        self.assertTrue(Tree.DeleteNodeByKey(11))                
        self.assertTrue(Tree.DeleteNodeByKey(10))                
        Array_Wide_3 = [8, 4, 12, 2, 6, 14, 3, 5, 7, 13, 15]    # теперь тестовый массив будет выгляеть так       
        res = Tree.WideAllNodes()
        for i in range (len(res)):                              
            self.assertEqual(res[i].NodeKey, Array_Wide_3[i])     # проверка результата        

        self.assertTrue(Tree.DeleteNodeByKey(5))                # Удалим всю ветку F(6) 
        self.assertTrue(Tree.DeleteNodeByKey(7))                
        self.assertTrue(Tree.DeleteNodeByKey(6))                
        Array_Wide_4 = [8, 4, 12, 2, 14, 3, 13, 15]             # теперь тестовый массив будет выгляеть так       
        res = Tree.WideAllNodes()
        for i in range (len(res)):                              
            self.assertEqual(res[i].NodeKey, Array_Wide_4[i])     # проверка результата

        self.assertTrue(Tree.DeleteNodeByKey(12))                # Удаляем узел 12. На его место встанет узел 14. Узлы 13 и 15 сместятся на уровень выше
        Array_Wide_5 = [8, 4, 14, 2, 13, 15, 3]                 # теперь тестовый массив будет выгляеть так       
        res = Tree.WideAllNodes()
        for i in range (len(res)):                              
            self.assertEqual(res[i].NodeKey, Array_Wide_5[i])     # проверка результата 

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
