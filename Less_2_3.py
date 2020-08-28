class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0

class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey_Branch(self, Node, key):
        result = BSTFind()
        if Node.NodeKey == key:                                     # Ключ совпал
            result.Node = Node
            result.NodeHasKey = True
        elif Node.NodeKey > key and Node.LeftChild is not None:     # Ключ меньше, существует левый потомок
            result = self.FindNodeByKey_Branch(Node.LeftChild, key)
        elif Node.NodeKey > key and Node.LeftChild is None:         # Ключ меньше, отсутствует левый потомок 
            result.Node = Node
            result.ToLeft = True
        elif Node.NodeKey < key and Node.RightChild is not None:    # Ключ больше, существует правый потомок
            result = self.FindNodeByKey_Branch(Node.RightChild, key)
        elif Node.NodeKey < key and Node.RightChild is None:        # Ключ больше, отсутствует правый потомок
            result.Node = Node
        return result
                                                                        
    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        result = BSTFind()
        current = self.Root
        if current is None:
            return result
        return self.FindNodeByKey_Branch(current, key)

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        target = self.FindNodeByKey(key)
        if target.Node is None:                                     # Для вставки в пустое дерево
            self.Root = BSTNode(key, val, None)                     # Элемент формируется и становится корнем дерева
            self.Root.Level = 1
            return True
        elif not target.NodeHasKey  and target.ToLeft:                # Если ключ не найден и надо добавлять левого потомка
            target.Node.LeftChild = BSTNode(key, val, target.Node)
            target.Node.LeftChild.Level = target.Node.Level + 1
            return True
        elif not target.NodeHasKey:                                 # Если ключ не найден и надо добавлять правого потомка
            target.Node.RightChild = BSTNode(key, val, target.Node)
            target.Node.RightChild.Level = target.Node.Level + 1
            return True
        return False                                                # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        current = FromNode
        if current is None:
            return None                                             # для пустого дерева
        elif FindMax and current.RightChild is None:
            return current
        elif FindMax:   
            return self.FinMinMax(current.RightChild, FindMax)
        elif current.LeftChild is None:
            return current
        else:
            return self.FinMinMax(current.LeftChild, FindMax)        
   
    def level_Node(self, Node):                 # Определение уровня проверяемого узла
        levels = 1
        if Node.Parent is None:
            return levels
        else:
            return levels + self.level_Node(Node.Parent)

    def level_branch(self, Node):               # Запись в соотв. поле уровня текущего узла и его детей
        Node.Level = self.level_Node(Node)
        if Node.LeftChild is not None:              # Если проверяемый узел имеет левого потомка
            self.level_branch(Node.LeftChild)       # рекурсивно - для всей левой ветки определяем уровни
        if Node.RightChild is not None:              # Если проверяемый узел имеет правого потомка
            self.level_branch(Node.RightChild)       # рекурсивно - для всей правой ветки определяем уровни
                
    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        removed = self.FindNodeByKey(key)
        if not removed.NodeHasKey:                  # если узел не найден
            return False
        # Рассмотрим удаление корня
        if removed.Node.Parent is None:
            if removed.Node.LeftChild is None and removed.Node.RightChild is None:              # удаляется лист 
                self.Root = None
            elif removed.Node.LeftChild is None and removed.Node.RightChild is not None:        # есть только 1 правый потомок
                removed.Node.RightChild.Parent = None
                self.Root = removed.Node.RightChild
                self.Root.Level = 1
                self.level_branch(self.Root)
            elif removed.Node.RightChild is None and removed.Node.LeftChild is not None:    # есть только 1 левы1 потомок
                removed.Node.LeftChild.Parent = None
                self.Root = removed.Node.LeftChild
                self.level_branch(self.Root)
            else:                                                                               # есть оба потомка
                heir = self.FinMinMax(removed.Node.RightChild, False)           # Находим преемника
                removed.Node.NodeKey = heir.NodeKey
                removed.Node.NodeValue = heir.NodeValue                         # Переписываем содержание преемника в удаляемый узел
                if heir.RightChild is not None:                                 # если у преемника есть потомки
                    heir.RightChild.Parent = heir.Parent                        # "перевешиваем" их родителю преемника
                    if heir.Parent.NodeKey > heir.NodeKey:
                        heir.Parent.LeftChild = heir.RightChild
                    else:
                        heir.Parent.RightChild = heir.RightChild
                else:                                                           # а если преемник - лист, то у его родителя обнуляем ссылку на heir
                    if heir.Parent.NodeKey > heir.NodeKey:
                        heir.Parent.LeftChild = None
                    else:
                        heir.Parent.RightChild = None
                self.level_branch(self.Root)
        else:
            # Далее рассмотрим случаи когда удаляемый элемент - не корневой
            if removed.Node.LeftChild is None and removed.Node.RightChild is None and removed.Node.NodeKey < removed.Node.Parent.NodeKey:
                # удаляется левый лист
                removed.Node.Parent.LeftChild = None
            elif removed.Node.LeftChild is not None and removed.Node.RightChild is None and removed.Node.NodeKey < removed.Node.Parent.NodeKey:
                # удаляется левый узел с 1 левым потомком
                removed.Node.Parent.LeftChild = removed.Node.LeftChild
                removed.Node.LeftChild.Parent = removed.Node.Parent         # Перевешиваем потомка к родителю
                self.level_branch(removed.Node.Parent.LeftChild)            # перезаписываем уровни в перевешенной ветке
            elif removed.Node.LeftChild is None and removed.Node.RightChild is not None and removed.Node.NodeKey < removed.Node.Parent.NodeKey:
                # удаляется левый узел с 1 правым потомком
                removed.Node.Parent.LeftChild = removed.Node.RightChild
                removed.Node.RightChild.Parent = removed.Node.Parent        # Перевешиваем потомка к родителю
                self.level_branch(removed.Node.Parent.LeftChild)            # перезаписываем уровни в перевешенной ветке
            elif removed.Node.LeftChild is None and removed.Node.RightChild is None and removed.Node.NodeKey > removed.Node.Parent.NodeKey:
                # удаляется правый лист.
                removed.Node.Parent.RightChild = None
            elif removed.Node.LeftChild is not None and removed.Node.RightChild is None and removed.Node.NodeKey > removed.Node.Parent.NodeKey:
                # удаляется правый узел с 1 левым потомком
                removed.Node.Parent.RightChild = removed.Node.LeftChild
                removed.Node.LeftChild.Parent = removed.Node.Parent         # Перевешиваем потомка к родителю
                self.level_branch(removed.Node.Parent.RightChild)           # перезаписываем уровни в перевешенной ветке
            elif removed.Node.LeftChild is None and removed.Node.RightChild is not None and removed.Node.NodeKey > removed.Node.Parent.NodeKey:
                # удаляется правый узел с 1 правым потоском
                removed.Node.Parent.RightChild = removed.Node.RightChild
                removed.Node.RightChild.Parent = removed.Node.Parent     # Перевешиваем потомка к родителю
                self.level_branch(removed.Node.Parent.RightChild)           # перезаписываем уровни в перевешенной ветке
            elif removed.Node.LeftChild is not None and removed.Node.RightChild is not None:
                # удаляется узел с двумя потомками
                heir = self.FinMinMax(removed.Node.RightChild, False)           # Находим преемника
                removed.Node.NodeKey = heir.NodeKey
                removed.Node.NodeValue = heir.NodeValue                         # Переписываем содержание преемника в удаляемый узел
                if heir.RightChild is not None:                                 # если у преемника есть потомки
                    heir.RightChild.Parent = heir.Parent                        # "перевешиваем" их родителю преемника
                    if heir.Parent.NodeKey > heir.NodeKey:
                        heir.Parent.LeftChild = heir.RightChild
                    else:
                        heir.Parent.RightChild = heir.RightChild
                    self.level_branch(heir.RightChild)                          # перезаписываем уровни в перевешенной ветке
                else:                                                           # а если преемник - лист, то у его родителя обнуляем ссылку на heir
                    if heir.Parent.NodeKey > heir.NodeKey:
                        heir.Parent.LeftChild = None
                    else:
                        heir.Parent.RightChild = None
        return True
    
    def Count_branch(self, Node):
        counter = 0
        if Node.LeftChild is not None:                      # Если проверяемый узел имеет левого потомка
            counter += self.Count_branch(Node.LeftChild)
        if Node.RightChild is not None:                     # Если проверяемый узел имеет левого потомка
            counter += self.Count_branch(Node.RightChild)               
        return counter + 1                                  # не забыть про самого себя
            
    def Count(self):
        # количество всех узлов в дереве
        if self.Root is None:
            return 0
        counter = 0                                    
        if self.Root.LeftChild is not None:                      # Если проверяемый узел имеет левого потомка
            counter += self.Count_branch(self.Root.LeftChild)
        if self.Root.RightChild is not None:                     # Если проверяемый узел имеет левого потомка
            counter += self.Count_branch(self.Root.RightChild)               
        return counter + 1

    def DeepNodesBranch(self, Node, option):
        current = Node
        result = tuple()
        if option == 0:
            # in-order
            if current.LeftChild is not None:
                result += self.DeepNodesBranch(current.LeftChild, option)
            result += (current,)
            if current.RightChild is not None:
                result += self.DeepNodesBranch(current.RightChild, option)
        elif option == 1:
            # post-order
            if current.LeftChild is not None:
                result += self.DeepNodesBranch(current.LeftChild, option)
            if current.RightChild is not None:
                result += self.DeepNodesBranch(current.RightChild, option)
            result += (current,)
        elif option == 2:
            # pre-order
            result += (current,)
            if current.LeftChild is not None:
                result += self.DeepNodesBranch(current.LeftChild, option)
            if current.RightChild is not None:
                result += self.DeepNodesBranch(current.RightChild, option)
        return result
        
    def DeepAllNodes(self, option):
        result = tuple()
        if option == 0:
            # in-order
            if self.Root.LeftChild is not None:
                result += self.DeepNodesBranch(self.Root.LeftChild, option)
            result += (self.Root,)
            if self.Root.RightChild is not None:
                result += self.DeepNodesBranch(self.Root.RightChild, option)
        elif option == 1:
            # post-order
            if self.Root.LeftChild is not None:
                result += self.DeepNodesBranch(self.Root.LeftChild, option)
            if self.Root.RightChild is not None:
                result += self.DeepNodesBranch(self.Root.RightChild, option)
            result += (self.Root,)
        elif option == 2:
            # pre-order
            result += (self.Root,)
            if self.Root.LeftChild is not None:
                result += self.DeepNodesBranch(self.Root.LeftChild, option)
            if self.Root.RightChild is not None:
                result += self.DeepNodesBranch(self.Root.RightChild, option)
        return result        

    def WideAllNodes(self):
        result = tuple()
        # сначала сформируем двумерный массив для распределения узлов по уровням
        Matrix = [[]]                               # создаем матрицу уровней
        count = 0                                   # и счетчик для нее
        if self.Root is not None:                   # начинаем с корня
            Matrix[0].append(self.Root)
            count += 1
        while count < self.Count():                 # мы перебирем все узлы дерева
            Matrix.append([])                       # добавляем список для нового уровня
            for i in Matrix[-2]:                    # пробегаем по всем узлам предыдущего уровня
                if i.LeftChild is not None:
                    Matrix[-1].append(i.LeftChild)
                    count += 1
                if i.RightChild is not None:
                    Matrix[-1].append(i.RightChild)
                    count += 1
        if len(Matrix[-1]) == 0:                    # на последнем шаге (когда обходим только листы) список для следующего уровня останется пустым
            Matrix.pop()                            # удалим его
        # Теперь - второй этап. Надо превратить матрицу в линейный кортеж
        for i in Matrix:
            for j in i:
                result += (j,)                  # воспользуемся конкатенацией               
        return result
