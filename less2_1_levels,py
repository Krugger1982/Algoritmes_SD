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

    def AddChild(self, ParentNode, NewChild):
        # ваш код добавления нового дочернего узла существующему ParentNode
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
        self.level_branch(Node)
