class Vertex:

    def __init__(self, val):
        self.Value = val
  
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
