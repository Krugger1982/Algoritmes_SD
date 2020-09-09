class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key      # ключ узла
        self.Parent = parent    # родитель или None для корня
        self.LeftChild = None   # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0          # уровень узла
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева

    def GenerateTree(self, a):
        # создаём дерево с нуля из неотсортированного массива a
        a.sort()                                # отсортируем массив а
        center = middle(a)
        if center is None:
            return None
        self.Root = BSTNode(a[center], None)    # создаем корень дерева
        self.Root.Level = 1                     # У корня уровень равен 1
        leftList = a[:center]
        rightList = a[(center + 1):]
        self.Root.LeftChild = self.GenerateBranch(leftList, self.Root)      # для левого потомка берем срез левее (меньше) чем середина, center не входит
        self.Root.RightChild = self.GenerateBranch(rightList, self.Root)    # для правого потомка берем срез правее (больше) чем середина, center не входит

    def GenerateBranch(self, a, Node):
        # рекурсивная функция для поддеревьев (веток)
        index = middle(a)
        if index is None:                                                       # если на входе пустой массив
            return None                                                         # то результатом будет пустая ветка
        current = BSTNode(a[index], Node)                                       # создаем узел из ключа a[index] и подвешиваем полученный узел к родителю - Node
        current.Level = Node.Level + 1
        leftList = a[:index]
        rightList = a[index + 1:]
        current.LeftChild = self.GenerateBranch(leftList, current)          # для левого потомка берем срез левее (меньше) чем середина, index не входит
        current.RightChild = self.GenerateBranch(rightList, current)        # для правого потомка берем срез правее (больше) чем середина, index не входит
        return current

    def MinMax(self, node):         # функция для обхода ветки
        if node is None:
            return [0, 0]           # пустое дерево имеет глубину 0 и верхний незаполненный узел на уровне 0
        Left = self.MinMax(node.LeftChild)          
        Right = self.MinMax(node.RightChild)
        if node.LeftChild is None and node.RightChild is None:          # если узел - лист
            MaxLevel = node.Level                                       # то возвращаем его уровень
        else:
            MaxLevel = max(Left[0], Right[0])
            # находим максимальную глубину сравнивая макс. глубины поддеревьев
        if  node.LeftChild is None or node.RightChild is None:          # если в узле не хватает хотя бы одного потомка (узел неполный или лист)
            MinLevel = node.Level                                       # то возвращаем его уровень
        else:                                                           # а если есть оба потомка
            MinLevel = min(Left[1], Right[1])                           # то спускаемся на уровень ниже
        return [MaxLevel, MinLevel]
        
    def IsBalanced(self, root_node):
        if root_node == None:
            return True             # пустое дерево сбалансировано по умолчанию
        result = self.MinMax(root_node)
        return (result[0] - result[1]) <= 1
        
def middle(a):
    if len(a) == 0:
        return None
    if len(a) == 1:
        return 0
    result = (len(a) - 1)//2                # для четного количества элементов серединой выбираем левого из двух центральных
    if (len(a) == 3 or len(a) == 4) and a[0] != a[1]:        # подмассив размером  3 или 4 при неравенстве первых двух членов автоматически балансируется
        result = 1                          
    elif (0 < result < (len(a) - 1)) and (a[result] == a[result - 1] or a[result] == a[result + 1]) and a[-1] > a[result]:
        # если result находится в середине массива и попал в повтор, то идем к ближайшему правому, отличному от повторяющихся
        # тогда ряд повторов окажется в правом конце левого подмассива (правые листья)
        result += 1
        while a[result] == a[result - 1] and result < len(a)-1:
            result += 1
    elif (0 < result < (len(a) - 1)) and (a[result] == a[result - 1] or a[result] == a[result + 1]) and a[result] == a[-1]  and a[0] < a[result]:
        # если result находится в середине массива и попал в повтор и правее его нету отличающегося элемента то идем к самому левому из  повторяющихся
        while a[result] == a[result - 1]:
            result -= 1
        if result == 0:                 # если этим "ближайшим левым" оказался самый первый элемент
            result = 1                  # тогда центром берем самый левый из повторяющихся,
                                        # тогда ряд повторов вытянется в лозу, а единственный "ближайший левый" станет левым потомком этого центра        
    elif a[result] == a[result - 1] or a[result] == a[result + 1]:
        # если result попал в повтор, а ни слева ни справа нет элементов, отличных от result, то есть весь подмассив состоит из одинаковых элементов
        # тогда идем к самому левому из повторяюшихся, то есть в начало массива
        result = 0
    # в остальных случаях двигать result  не требуется
    return result
