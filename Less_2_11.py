class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = 0
        
class Stack:

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    
    def push(self, value):
        self.stack.append(value)

class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        # ваш код добавления новой вершины 
        # с значением value 
        # в свободное место массива vertex
        Vert = Vertex(v)                                    # создаем вершину Vert
        index = self.vertex.index(None)                     # находим ближайшее свободное место в списке Vertex
        if index != -1:
            self.vertex[index] = Vert                       # и вставляем на это место вершину Vert 
	
    def RemoveVertex(self, v):
        for i in self.m_adjacency:                  # пробегаем по 1 измерению - строки матрицы
            i[v] = 0                                # и обнуляем v-тый столбец
        self.m_adjacency[v] = [0] * self.max_vertex # а потом обнуляем v-тую строку
        self.vertex[v] = None                       # и удаляем вершину из списка
	
    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1]
	
    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        # в матрице смежности напротив этих индексов проставляем 1
        self.m_adjacency[v1][v2] = 1
        if v1 != v2:
            self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        # в матрице смежности напротив этих индексов проставляем 0
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        result = Stack()
        for Vertexes in self.vertex:
            if Vertexes is not None:
                Vertexes.Hit = False            # помечаем все существующие вершины графа как непосещенные
        self.vertex[VFrom].Hit += 1             # посещаем исходную вершину 
        result.push(self.vertex[VFrom])         # заносим ее в "Путь"
        if self.m_adjacency[VFrom][VTo] == 1:   # если искомая вершина - смежная с текущей
            result.push(self.vertex[VTo])          # то просто добавляем ее в "путь"
            return result.stack
        for Nearby in range(len(self.m_adjacency[VFrom])):      # пробегаем по строчке в матрице смежности, которая соответствует VFrom
            if (self.m_adjacency[VFrom][Nearby] == 1 and  self.vertex[Nearby].Hit == 0               # рассматриваем только непосещенные смежные узлы
                and result.size() - self.Search_Way_recourcive(Nearby, VTo, result).size() != 0):
            # Если в результате поиска в очередном узле размер пути изменился, то путь найден
                return result.stack
        return []   # если путь не найден, возвращаем пустой список

    def Search_Way_recourcive(self, VFrom, VTo, Way):
        '''рекурсивный метод для поиска куска пути без предварительных очисток'''
        self.vertex[VFrom].Hit += 1                                 # посещаем исходную вершину 
        Way.push(self.vertex[VFrom])                                # заносим ее в "Путь"
        if self.m_adjacency[VFrom][VTo] == 1:                       # если искомая вершина - смежная с текущей
            Way.push(self.vertex[VTo])                              # то просто добавляем ее в "путь"
            return Way
        for Nearby in range(len(self.m_adjacency[VFrom])):                                  # пробегаем по строчке в матрице смежности, которая соответствует VFrom
            if (self.m_adjacency[VFrom][Nearby] == 1 and self.vertex[Nearby].Hit == 0
                and Way.size() - self.Search_Way_recourcive(Nearby, VTo, Way).size() != 0):
            # Если в результате поиска в очередном непосещенном узле размер пути изменился, то путь найден
                return Way
        Way.pop()       # В противном случае - делаем вывод: из этого узла пути нет
                        # Удаляем этот узел из стека
        return Way

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        for Vertexes in self.vertex:
            if Vertexes is not None:
                Vertexes.Hit = 0                # обнуляем у все
        result = []                             # создаем список для записи вершин
        current = VFrom
        self.vertex[current].Hit = 1            # помечаем стартовую вершину как посещенную, 1 уровня
        result.append(current)                  # заносим ее индекс в список
                      
        while len(result) > 0:                 # начинаем перебор элементов графа "волнами", с проставлением номеров шага 
            current = result.pop(0)                                                             # выдергиваем из списка текушую вершину
            for Nearby in range(len(self.m_adjacency[current])):                                # пробегаем по строке очередной вершины в матрице смежности
                if (self.m_adjacency[current][Nearby]) == 1 and self.vertex[Nearby].Hit == 0:   # Перебирам всех непосещенных смежных с текущей вершиной
                    self.vertex[Nearby].Hit  = self.vertex[current].Hit  + 1                    # присваиваем посещенной вершине уровень - на 1 больше чем у current
                    result.append(Nearby)                                                       # вставляем посещенную вершину (ее индекс) в result
        # цикл закончится, когда мы обойдем все элементы, связные с VFrom (до кого можно добраться)
        # для того чтоб определить кратчайший путь из нескольких, пройдем по вершинам обратно,
        # от вершины Vto через смежные - и до вершины VFrom
        # на обратном пути из смежных выбираем ту, у которой наименьший уровень в поле .Hits
        current = VTo                                 
        if self.vertex[current].Hit > 0:                                        # если в вершине Vto проставлен уровень, значит путь есть.
            while current !=  VFrom:                                            # идем обратно пока не доберемся до VFrom
                result.append(self.vertex[current])
                Previous_steps = []                                                                     # список для выбора из нескольких вариантов пред. шага
                for Nearby in range(len(self.m_adjacency[current])):                                    # перебираем строчку в матрице смежности
                    if (self.m_adjacency[current][Nearby]) == 1 and self.vertex[Nearby].Hit > 0 and self.vertex[Nearby].Hit < self.vertex[current].Hit:
                    # выбираем посещенные и смежные вершины с меньшими уровнями чем current
                        Previous_steps.append([self.vertex[Nearby].Hit, self.vertex[Nearby]])           # записываем в список пару - [значание Hits, вершина]
                for i in range(len(Previous_steps)):                            # Находим вершину с минимальным значением Hits
                    if i == 0:
                        Min_Hit = Previous_steps[i][0]
                        Min_Hit_Vertex = Previous_steps[i][1]
                    elif Previous_steps[i][0] < Min_Hit:
                        Min_Hit = Previous_steps[i][0]
                        Min_Hit_Vertex = Previous_steps[i][1]                                                       
                current = self.vertex.index(Min_Hit_Vertex)                     # Задаем новое значение current
            result.append(self.vertex[VFrom])
            result.reverse()
        return result
