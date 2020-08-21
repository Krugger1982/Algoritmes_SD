class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
        self.Level = 0
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root; # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild):
        # ваш код добавления нового дочернего узла существующему ParentNode
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
        
  
    def DeleteNode(self, NodeToDelete):
        # ваш код удаления существующего узла NodeToDelete
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def Get_All_Nodes_branch(self, Node):
        result = []
        result.append(Node)
        if len(Node.Children) != 0:             # Если проверяемый узел - лист, то считаем только его
            for i in Node.Children:             # В противном случае записываем все его поддеревья 
                result = result + self.Get_All_Nodes_branch(i)
        return result                           
        
    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        result = []
        if self.Root is None:               
            return []
        result.append(self.Root)                        # Вносим в список корень
        for current in self.Root.Children:              # пройдемся по веткам (если они есть)
            result = result + self.Get_All_Nodes_branch(current)   
        return result

    def Find_values_branch(self, Node, val):
        result = []
        if Node.NodeValue == val:
            result.append(Node)
        if len(Node.Children) != 0:             
            for i in Node.Children:               
                result = result + self.Find_values_branch(i, val)
        return result                           

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        result = []
        if self.Root is None:               
            return []
        if self.Root.NodeValue == val:
            result.append(self.Root)
        for current in self.Root.Children:
            result = result + self.Find_values_branch(current, val)
        return result
   
    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
          
    def Count_branch(self, Node):
        counter = 0
        if len(Node.Children) != 0:             # Если проверяемый узел - лист, то считаем только его
            for i in Node.Children:             # В противном случае считаем все его поддеревья 
                counter += self.Count_branch(i)
        return counter + 1                      # и его самого
            
    def Count(self):
        # количество всех узлов в дереве
        result = 0
        if self.Root is None:
            return 0
        result += 1                                 # считаем корень
        for current in self.Root.Children:
            result += self.Count_branch(current)         # обходим и считаем детей
        return result

    def Leaf_Count_branch(self, Node):
        counter = 0
        if len(Node.Children) == 0:
            counter += 1
        else:
            for current in Node.Children:
                counter += self.Leaf_Count_branch(current)
        return counter

    def LeafCount(self):
        # количество листьев в дереве
        counter = 0
        if len(self.Root.Children) == 0:
            counter += 1
        else:
            for current in self.Root.Children:
                counter += self.Leaf_Count_branch(current)
        return counter

    def level_Node(self, Node):                 # Определение уровня проверяемого узла
        levels = 1
        if Node.Parent is None:
            return levels
        else:
            return levels + self.level_Node(Node.Parent)
        
    def level_branch(self, Node):               # Запись в соотв. поле уровня текущего узла и его детей
        Node.Level = self.level_Node(Node)
        if len(Node.Children) != 0:             # Если проверяемый узел имеет детей
            for current in Node.Children:       # тогда для каждого "потомка" определяем уровни 
                self.level_branch(current)      # и рекурсивно - для всей ветки

    def Level_Tree(self):
        # Прописываем уровни для всех узлов дерева
        self.Root.Level = 1
        for current in self.Root.Children:
            self.level_branch(current)
