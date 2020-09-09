import unittest

class MyTestCase(unittest.TestCase):
    def test_1_middle(self):
        a = [0, 1, 2, 3, 4, 5, 6, 7]                # массив с четным количеством элементов
        self.assertEqual(a[middle(a)], 3)           # проверка - возвращается индекс элемента, содержащего 3 (левый из 2х средних)
        
        a = []                                      # пустой масив
        self.assertEqual(middle(a), None)           # проверка - возвращается None
        
        a = [8]                                     # массив с одним элементом
        self.assertEqual(middle(a), 0)              # проверка - возвращается индекс 0 - единственного элемента
        
        a = [0, 2, 4]                               # массив с нечетным количеством элементов
        self.assertEqual(middle(a), 1)              # проверка - возвращается индекс элемента, содержащего 2 (середина)
        
        a = [0, 1, 2, 2, 4, 5, 6, 7]                # массив с посторяющимися элементами в середине 
        self.assertEqual(middle(a), 4)              # проверка - возвращается индекс элемента, содержащего 4 (ближайший отличный справа)
 
        a = [0, 1, 2, 3, 3, 3, 3, 3]                # массив с пострияющимися элементами от центра и до конца
        self.assertEqual(middle(a), 3)              # проверка - возвращается индекс элемента, содержащего 2 (ближайший отличный слева)
        
        a = [0, 0, 0, 0, 0, 3, 3, 3]                # массив повторяющимися элементами от начала до центра
        self.assertEqual(middle(a), 5)              # проверка - возвращается индекс элемента, содержащего 5 (ближайший отличный справа)
        
        a = [0, 0, 0, 0, 0,]                        # массив со всеми одинаковыми элементами
        self.assertEqual(middle(a), 0)              # проверка - возвращается индекс самого левого из повторяющихся, в данном случае 0

        a = [1, 2, 2, 5]                            # исключение массив размерм 4 с повтором внутри и отличающимися элементами по краям
        self.assertEqual(middle(a), 1)              # проверка - возвращается индекс самого левого из повторяющихся, в данном случае 1

        a = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8]       
        self.assertEqual(middle(a), 5)
        a = [0, 1, 1, 2, 2]
        self.assertEqual(middle(a), 3)
        a = [0, 1, 1, 1]
        self.assertEqual(middle(a), 1)

    def test_2_generate_empty (self):
        # создадим пустой тестовый массив
        a = []          
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #
        #           Root (None)
        #              
        #
        current = b.Root                                # находимся в корне
        self.assertEqual(current, None)                 # проверка - корнем является None
        self.assertTrue(b.IsBalanced(b.Root))

    def test_3_generate_alone_Node(self):
        # создадим тестовый массив из одного элемента
        a = []
        a.append(15)
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #
        #           Root (15)
        #           /     \
        #       None      None
        current = b.Root                                # находимся в корне
        self.assertEqual(current.NodeKey, 15)           # проверка - в корне хранится 15
        self.assertEqual(current.LeftChild, None)       # его левый потомок - None
        self.assertEqual(current.RightChild, None)      # его правый потомок - None

    def test_4_generate_simpleTree(self):
        a = [15, 20, 28]          
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #
        #    Root    (20)
        #           /    \
        #       (15)      (28)
        #      /   \      /    \
        #   None  None  None  None
        #
        current = b.Root                                # находимся в корне
        self.assertEqual(current.NodeKey, 20)           # проверка - в корне хранится 20
        self.assertEqual(current.LeftChild.NodeKey, 15)         # его левый потомок хранит 15
        self.assertEqual(current.LeftChild.LeftChild, None)
        self.assertEqual(current.LeftChild.RightChild, None)    # потомки узла 15 являются None
        self.assertEqual(current.RightChild.NodeKey, 28)        # его правый потомок хранит 28
        self.assertEqual(current.RightChild.LeftChild, None)
        self.assertEqual(current.RightChild.RightChild, None)   # потомки узла 28 являются None

    def test_5_generate(self):
        # создадим тестовый массив с повторами элементов
        a = [4, 0, 1, 7, 1, 2, 5,  8, 2, 6, 3]          # отсортировав получим [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8]
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #           Root (3)
        #              /     \
        #           (2)       (6)
        #          /   \     /   \
        #       (1)    (2) (4)    (7)
        #       / \          \      \  
        #     (0) (1)        (5)    (8)
        #
        current = b.Root                                # находимся в корне
        self.assertEqual(current.NodeKey, 3)            # проверка - в корне хранится 3
        
        current = current.LeftChild                     # смещаемся в узел 2
        self.assertEqual(current.NodeKey, 2)            # проверка - в узле хранится 2
        
        current = current.LeftChild                     # смещаемся в узел 1
        self.assertEqual(current.NodeKey, 1)            # проверка - в узле хранится 1
        self.assertEqual(current.LeftChild.NodeKey, 0)              # проверка - в его левом потомке хранится 0
        self.assertEqual(current.RightChild.NodeKey, 1)             # проверка - в его правом потомке хранится 1
        
        current = b.Root.LeftChild.RightChild           # смещаемся в узел 2 (нижний)
        self.assertEqual(current.NodeKey, 2)            # проверка - в узле хранится 2
        
        current = b.Root.RightChild                     # смещаемся в правое поддерево - узел 6
        self.assertEqual(current.NodeKey, 6)            # проверка - в узле хранится 6
        
        current = current.LeftChild                     # смещаемся в узел 4
        self.assertEqual(current.NodeKey, 4)            # проверка - в узле хранится 4
        self.assertEqual(current.LeftChild, None)       # а его левый потомок указывает на None
        
        current = current.RightChild                    # смещаемся в узел 5
        self.assertEqual(current.NodeKey, 5)            # проверка - в узле хранится 5
        self.assertEqual(current.LeftChild, None)
        self.assertEqual(current.RightChild, None)      # а его потомки указывают на None
        
        current = b.Root.RightChild.RightChild          # смещаемся в узел 7
        self.assertEqual(current.NodeKey, 7)            # проверка - в узле хранится 7
        self.assertEqual(current.RightChild .NodeKey, 8)# проверка - в его правом потомке хранится 8
        self.assertEqual(current.LeftChild, None)       # а его левый потомок указывает на None   .
        
    def test_6_generate_grapevine(self):
        a = [0, 1, 1, 1]
        self.assertEqual(middle(a), 1)
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #           Root (1)
        #               /   \
        #            (0)     (1)
        #                      \
        #                       (1)
        current = b.Root                                # находимся в корне
        self.assertEqual(current.NodeKey, 1)            # проверка - в корне хранится 1
        current = current.LeftChild                     # смещаемся в узел 0
        self.assertEqual(current.NodeKey, 0)            # проверка - в узле хранится 0
        self.assertEqual(current.LeftChild, None)
        self.assertEqual(current.RightChild, None)      # а его потомки указывают на None
        current = b.Root.RightChild                     # смещаемся в узел 1 (средний)
        self.assertEqual(current.NodeKey, 1)            # проверка - в узле хранится 0
        self.assertEqual(current.LeftChild, None)       # а его левый потомок указывает на None
        current = current.RightChild                    # смещаемся в узел 1 (нижний)
        self.assertEqual(current.NodeKey, 1)            # проверка - в узле хранится 1
        self.assertEqual(current.LeftChild, None)
        self.assertEqual(current.RightChild, None)      # а его потомки указывают на None        

    def test_7_balanced_empty (self):
        # создадим пустой тестовый массив
        a = []          
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #
        #           Root (None)
        #              
        current = b.Root                                # находимся в корне
        self.assertEqual(current, None)                 # проверка - корнем является None
        self.assertTrue(b.IsBalanced(b.Root))           # проверка - пустое дерево сбалансированно

    def test_8_balanced_alone_element(self):
        # создадим тестовый массив из одного элемента
        a = [15]
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #
        #           Root (15)
        #           /     \
        #       None      None
        
        self.assertTrue(b.IsBalanced(b.Root))           # проверка - дерево сбалансированно


    def test_9_balanced(self):
        # создадим тестовый массив с повторами элементов
        a = [4, 0, 1, 7, 1, 2, 5,  8, 2, 6, 3]          # отсортировав получим [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8]
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #           Root (3)
        #              /     \
        #           (2)       (6)
        #          /   \     /   \
        #       (1)    (2) (4)    (7)
        #       / \          \      \  
        #     (0) (1)        (5)    (8)
        
        self.assertTrue(b.IsBalanced(b.Root))           # проверка -  дерево сбалансированно
        
    def test_10_not_balanced(self):
        # создадим тестовый массив с большим количеством повторов
        a = [1, 1, 0, 1, 1]                             # отсортировав получим [0, 1, 1, 1, 1 ]
        b = BalancedBST()                               # создаем пустое дерево
        b.GenerateTree(a)                               # генерируем BST из массива а
        # Должно получиться такое дерево:
        #           Root (1)
        #               /   \
        #            (0)     (1)
        #                      \
        #                       (1)
        #                         \
        #                         (1)

        self.assertFalse(b.IsBalanced(b.Root))           # проверка -  дерево не сбалансированно

        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
