import unittest

class MyTestCase(unittest.TestCase):

    def test_1_Not_Event_Tree (self):
        # создаем нечетное дерево
        #           Root(12)
        #           /\
        #       A(1)  B(2)
        #       /|\     \
        #      / | \     F(2)
        #     /  |  \
        # C(3)  D(2) E(4)
        #
        # тогда список для разрыва дерева на маленькие четные деревья будет выглядеть так:
        TestResultValues = [12, 1, 12, 2]
        #


        Root = SimpleTreeNode(12, None)
        Tree = SimpleTree(Root)
        NodeA = SimpleTreeNode(1, None)
        Tree.AddChild(Root, NodeA)
        NodeB = SimpleTreeNode(2, None)
        Tree.AddChild(Root, NodeB)
        NodeC = SimpleTreeNode(3, None)
        Tree.AddChild(NodeA, NodeC)
        NodeD = SimpleTreeNode(2, None)
        Tree.AddChild(NodeA, NodeD)
        NodeE = SimpleTreeNode(4, None)
        Tree.AddChild(NodeA, NodeE)
        NodeF = SimpleTreeNode(2, None)
        Tree.AddChild(NodeB, NodeF)
        self.assertEqual(Tree.Count(), 7)       # проверка - количество узлов - 7

        List_Of_Trees = Tree.EvenTrees()
        
        for i in range(len(TestResultValues)):                                  # пробегаем по тестовому списку
            self.assertEqual(TestResultValues[i], List_Of_Trees[i].NodeValue)   # и сравниваем его элементы с элементами List_Of_Trees (Точнее с их содержимым)
        
    def test_2_Event_Tree (self):
        # создаем тестовое дерево, на этот раз четное
        #           A(99)
        #          /  |  \
        #       B(1) C(5) \
        #       /|\   |    H(33)
        #      / | \  D(6)  \
        #     /  |  \       I(34)
        # E(3)  F(2) G(4)     \
        #                     J(35)
        #  список для разрыва дерева на маленькие четные деревья будет выглядеть так:
        TestResultValues = [99, 1, 99, 5, 33, 34]
        


        A = SimpleTreeNode(99, None)
        Tree = SimpleTree(A)
        B = SimpleTreeNode(1, None)
        Tree.AddChild(A, B)
        C = SimpleTreeNode(5, None)
        Tree.AddChild(A, C)
        E = SimpleTreeNode(3, None)
        Tree.AddChild(B, E)
        F = SimpleTreeNode(2, None)
        Tree.AddChild(B, F)
        G = SimpleTreeNode(4, None)
        Tree.AddChild(B, G)
        D = SimpleTreeNode(6, None)
        Tree.AddChild(C, D)
        H = SimpleTreeNode(33, None)
        Tree.AddChild(A, H)
        I = SimpleTreeNode(34, None)
        Tree.AddChild(H, I)
        J = SimpleTreeNode(35, None)
        Tree.AddChild(I, J)
        self.assertEqual(Tree.Count(), 10)       # проверка - количество узлов - 10

        List_Of_Trees = Tree.EvenTrees()
        for i in range(len(TestResultValues)):                                  # пробегаем по тестовому списку
            self.assertEqual(TestResultValues[i], List_Of_Trees[i].NodeValue)   # и сравниваем его элементы с элементами List_Of_Trees (Точнее с их содержимым)    
