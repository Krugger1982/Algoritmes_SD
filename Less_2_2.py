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
        if removed.Node.Parent is None and removed.Node.LeftChild is None and removed.Node.RightChild is None:      # если корень - лист
            self.Root = None                                                            # в итоге - пустое дерево           
        elif removed.Node.Parent is None and removed.Node.LeftChild is None:            # если у корня есть только правый потомок
            self.Root = removed.Node.RightChild
            removed.Node.RightChild.Parent = None                                       # Этот потомок становится корнем
        elif removed.Node.Parent is None and removed.Node.RightChild is None:           # если у корня есть только левый потомок
            self.Root = removed.Node.LeftChild
            removed.Node.LeftChild.Parent = None                                        # Этот потомок становится корнем
        elif removed.Node.Parent is None:                                               # Если у корня 2 потомка
            heir = self.FinMinMax(removed.Node.RightChild, False)           # Находим преемника
            if heir.RightChild is not None:                            # Если у преемника есть правый сын
                heir.RightChild.Parent = heir.Parent                   # перевешиваем его к "отцу" преемника
                heir.Parent.LeftChild = heir.RightChild
            else:
                heir.Parent.LeftChild = None                                # А если преемник - лист, то у его родителя обнуляем ссылку на heir
            self.Root = heir                                                # и перемещаем преемника в корень
            heir.Parent = None                                              # связь с отцом - None
            heir.LeftChild = removed.Node.LeftChild                         # забираем детей от removed.None
            heir.RightChild = removed.Node.RightChild
        # Далее рассмотрим случаи когда удаляемый элемент - не корневой
        elif removed.Node.LeftChild is None and removed.Node.RightChild is None and removed.Node.Parent.NodeKey > removed.Node.NodeKey:    # Если удаляемый - левый лист
            removed.Node.Parent.LeftChild = None
        elif removed.Node.Parent.NodeKey < removed.Node.NodeKey:                                                                         # Если удаляемый - правый лист
            removed.Node.Parent.RightChild = None
        elif removed.Node.RightChild is None and removed.Node.Parent.NodeKey > removed.Node.NodeKey:     # Если удаляемый - левый потомок и у него есть только левый потомок
            removed.Node.LeftChild.Parent = removed.Node.Parent
            removed.Node.Parent.LeftChild = removed.Node.LeftChild
        elif removed.Node.LeftChild is None and removed.Node.Parent.NodeKey > removed.Node.NodeKey:      # Если удаляемый - левый потомок и у него есть только правый потомок
            removed.Node.RightChild.Parent = removed.Node.Parent
            removed.Node.Parent.LeftChild = removed.Node.RightChild
        elif removed.Node.Parent.NodeKey < removed.Node.NodeKey and removed.Node.RightChild is None:     # Если удаляемый правый потомок и у него есть только левый потомок
            removed.Node.LeftChild.parent = removed.Node.Parent
            removed.Node.Parent.RightChild = removed.Node.LeftChild
        elif removed.Node.Parent.NodeKey < removed.Node.NodeKey and removed.Node.LeftChild is None:      # Если удаляемый - правый потомок и у него есть только правый потомок
            removed.Node.RightChild.Parent = removed.Node.Parent
            removed.Node.Parent.RightChild = removed.Node.RightChild
        elif removed.Node.Parent.NodeKey > removed.Node.NodeKey:                            # Случай с двумя потомками,  удаляемый - левый
            heir = heir = self.FinMinMax(removed.Node.RightChild, False)                    # Находим преемника
            if heir.RightChild is not None:                                                 # механизм замещения, если у преемника есть правый потомок
                heir.RightChild.Parent = heir.Parent                                        # то перевешиваем его от heir к родителю heir
                heir.Parent.LeftChild = heir.RightChild
            else:
                heir.Parent.LeftChild = None                                                # А если преемник - лист, то у его родителя обнуляем ссылку на heir
            heir.Parent = removed.Node.Parent                                               # переносим связи с родителем
            heir.Parent.LeftChild = heir
            heir.LeftChild = removed.Node.LeftChild                                         # и связи с детьми
            heir.LeftChild.Parent = heir
            heir.RightChild = removed.Node.RightChild
            heir.RightChild.Parent = heir
        else:                                                                               # Случай с двумя потомками, удаляемый - правый
            heir = self.FinMinMax(removed.Node.RightChild, False)                    # Находим преемника
            if heir.RightChild is not None:                                            # механизм замещения, если у преемника есть правый потомок
                heir.RightChild.parent = heir.Parent            
                heir.Parent.LeftChild = heir.RightChild
            else:
                heir.Parent.LeftChild = None                                           # А если преемник - лист, то у его родителя обнуляем ссылку на heir
            heir.Parent = removed.Node.Parent                                          # переносим связи с родителем
            heir.Parent.RightChild = heir
            heir.LeftChild = removed.Node.LeftChild                                    # и связи с детьми
            heir.LeftChild.Parent = heir
            heir.RightChild = removed.Node.RightChild
            heir.RightChild.Parent = heir
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
