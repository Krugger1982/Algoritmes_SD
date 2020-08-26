class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


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
            return True
        elif not target.NodeHasKey  and target.ToLeft:                # Если ключ не найден и надо добавлять левого потомка
            target.Node.LeftChild = BSTNode(key, val, target.Node)
            return True
        elif not target.NodeHasKey:                                 # Если ключ не найден и надо добавлять правого потомка
            target.Node.RightChild = BSTNode(key, val, target.Node)
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
            elif removed.Node.RightChild is None and removed.Node.LeftChild is not None:    # есть только 1 левы1 потомок
                removed.Node.LeftChild.Parent = None
                self.Root = removed.Node.LeftChild
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
        else:
            # Далее рассмотрим случаи когда удаляемый элемент - не корневой
            if removed.Node.LeftChild is None and removed.Node.RightChild is None and removed.Node.NodeKey < removed.Node.Parent.NodeKey:
                # удаляется левый лист
                removed.Node.Parent.LeftChild = None
            elif removed.Node.LeftChild is not None and removed.Node.RightChild is None and removed.Node.NodeKey < removed.Node.Parent.NodeKey:
                # удаляется левый узел с 1 левым потомком
                removed.Node.Parent.LeftChild = removed.Node.LeftChild
                removed.Node.LeftChild.Parent = removed.Node.Parent     # Перевешиваем потомка к родителю
            elif removed.Node.LeftChild is None and removed.Node.RightChild is not None and removed.Node.NodeKey < removed.Node.Parent.NodeKey:
                # удаляется левый узел с 1 правым потомком
                removed.Node.Parent.LeftChild = removed.Node.RightChild
                removed.Node.RightChild.Parent = removed.Node.Parent     # Перевешиваем потомка к родителю
            elif removed.Node.LeftChild is None and removed.Node.RightChild is None and removed.Node.NodeKey > removed.Node.Parent.NodeKey:
                # удаляется правый лист.
                removed.Node.Parent.RightChild = None
            elif removed.Node.LeftChild is not None and removed.Node.RightChild is None and removed.Node.NodeKey > removed.Node.Parent.NodeKey:
                # удаляется правый узел с 1 левым потомком
                removed.Node.Parent.RightChild = removed.Node.LeftChild
                removed.Node.LeftChild.Parent = removed.Node.Parent     # Перевешиваем потомка к родителю
            elif removed.Node.LeftChild is None and removed.Node.RightChild is not None and removed.Node.NodeKey > removed.Node.Parent.NodeKey:
                # удаляется правый узел с 1 правым потоском
                removed.Node.Parent.RightChild = removed.Node.RightChild
                removed.Node.RightChild.Parent = removed.Node.Parent     # Перевешиваем потомка к родителю
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
