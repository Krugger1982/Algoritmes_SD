import unittest

class MyTestCase(unittest.TestCase):

    def test_1_add_and_Count (self):
        # создаем тестовое дерево
        #           Root(12)
        #           /\
        #       A(1)  B(2)
        #       /|\     \
        #      / | \     F(2)
        #     /  |  \
        # C(3)  D(2) E(4)

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
        self.assertEqual(Tree.Count(), 7)
        
    def test_2_add_child_LeafCount (self):
        # создаем тестовое дерево
        #           Root(12)
        #           /\
        #       A(1)  B(2)
        #       /|\     \
        #      / | \     F(2)
        #     /  |  \
        # C(3)  D(2) E(4)

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
        self.assertEqual(Tree.LeafCount(), 4)


    def test_3_add_child (self):
        # создаем тестовое дерево
        #           Root(12)
        #           /\
        #       A(1)  B(2)
        #       /|\     \
        #      / | \     F(2)
        #     /  |  \
        # C(3)  D(2) E(4)

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
        self.assertEqual(Tree.Count(), 7)
        self.assertEqual(Tree.LeafCount(), 4)
        NodesList = []                          # формируем тестовый список узлов в порядке "в глубину слева направо": [Root, A, C, D, E, B, F]
        NodesList.append(Root)
        NodesList.append(NodeA)
        NodesList.append(NodeC)
        NodesList.append(NodeD)
        NodesList.append(NodeE)
        NodesList.append(NodeB)
        NodesList.append(NodeF)
        Nodes_Tree = Tree.GetAllNodes()
        self.assertEqual(Nodes_Tree, NodesList)   # проверка списка полученных узлов дерева

    def test_4_delete_Node (self):
        # создаем тестовое дерево
        #           Root(12)
        #           /\
        #       A(1)  B(2)
        #       /|\     \
        #      / | \     F(2)
        #     /  |  \
        # C(3)  D(2) E(4)

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
        Tree.DeleteNode(NodeF)
        self.assertEqual(Tree.Count(), 6)

    def test_5_MoveNode (self):
        # создаем тестовое дерево
        #           Root(12)
        #           /\
        #       A(1)  B(2)
        #       /|\     \
        #      / | \     F(2)
        #     /  |  \
        # C(3)  D(2) E(4)

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
        Tree.MoveNode(NodeF, NodeA)             # перемещаем узел F в ветку А
        NodesList = []                          # формируем тестовый список узлов в порядке "в глубину слева направо": [Root, A, C, D, E, F, B]
        NodesList.append(Root)
        NodesList.append(NodeA)
        NodesList.append(NodeC)
        NodesList.append(NodeD)
        NodesList.append(NodeE)
        NodesList.append(NodeF)                 # Здесь узел F будет последним "ребенком" у узла А
        NodesList.append(NodeB)
        Nodes_Tree = Tree.GetAllNodes()
        self.assertEqual(Nodes_Tree, NodesList)   # проверка списка полученных узлов дерева        

    def test_6_Find_By_Value (self):
        # создаем тестовое дерево
        #           Root(12)
        #           /\
        #       A(1)  B(2)
        #       /|\     \
        #      / | \     F(2)
        #     /  |  \
        # C(3)  D(2) E(4)

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
        Nodes_Tree = Tree.FindNodesByValue(2)
        NodesList = []                          # формируем тестовый список искомых узлов в порядке "в глубину слева направо": [D, B, F]
        NodesList.append(NodeD)
        NodesList.append(NodeB)
        NodesList.append(NodeF)
        self.assertEqual(Nodes_Tree, NodesList)            # проверка списка полученных узлов дерева

    def test_7_Levels (self):
        # создаем тестовое дерево
        #          Root(12)
        #          /   \
        #       A(1)   B(2)
        #       /|\      \
        #      / | \     F(2)
        #     /  |  \
        # C(3)  D(2) E(4)

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
        Tree.Level_Tree()
        self.assertEqual(Tree.Root.Level, 1)
        self.assertEqual(NodeA.Level, 2)
        self.assertEqual(NodeB.Level, 2)
        self.assertEqual(NodeC.Level, 3)
        self.assertEqual(NodeD.Level, 3)
        self.assertEqual(NodeE.Level, 3)
        self.assertEqual(NodeF.Level, 3)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
