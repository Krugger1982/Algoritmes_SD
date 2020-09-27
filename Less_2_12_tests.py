import unittest

class MyTestCase(unittest.TestCase):

            
    def test_1_All_Treangles(self):
        # Создадим тестовый граф
        #       (0) ---(1)  
        #       /  \   /   \    
        #      /    (3) -- (2)
        #     /    /  \    /
        #   (5)--(4)   \  /
        #      \  |     (7)
        #       \ |       
        #        (6)     
        # Вершины расположены в списке по номерам:
        # TestGraph.vertex == [0, 1, 2, 3, 4, 5, 6, 7]
        # Так как все вершины графа состоят в треугольниках
        # то результатом поиска должен стать пустой список []
        
        TestGraph = SimpleGraph(15)      # создаем пустой граф
        TestGraph.AddVertex(0)          # добавляем вершину 0
        TestGraph.AddVertex(1)          # добавляем вершину 1
        TestGraph.AddVertex(2)          # добавляем вершину 2
        TestGraph.AddVertex(3)          # добавляем вершину 3
        TestGraph.AddVertex(4)          # добавляем вершину 4
        TestGraph.AddVertex(5)          # добавляем вершину 5
        TestGraph.AddVertex(6)          # добавляем вершину 6
        TestGraph.AddVertex(7)          # добавляем вершину 7

        TestGraph.AddEdge(0, 1)         # Добавляем ребра
        TestGraph.AddEdge(0, 3)
        TestGraph.AddEdge(0, 5)
        TestGraph.AddEdge(1, 2)
        TestGraph.AddEdge(1, 3)
        TestGraph.AddEdge(2, 3)
        TestGraph.AddEdge(2, 7)
        TestGraph.AddEdge(3, 4)
        TestGraph.AddEdge(3, 7)
        TestGraph.AddEdge(4, 5)
        TestGraph.AddEdge(4, 6)
        TestGraph.AddEdge(5, 6)

        self.assertEqual(TestGraph.WeakVertices(), [])   # проверка, результат - пустой список

     
    def test_2_Not_only_Treangles(self):
        # Создадим тестовый граф
        #       (0) ---(1)  
        #       /  \           
        #      /    (3) -- (2)
        #     /    /  \    /
        #   (5)--(4)   \  /
        #      \  |     (7)
        #       \ |      
        #        (6)--(8)
        # Вершины расположены в списке по номерам:
        # [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # Результатом поиска   должен стать такой список:
        Test_List1 = [0, 1, 8]
        
        TestGraph = SimpleGraph(20)      # создаем пустой граф
        TestGraph.AddVertex(0)          # добавляем вершину 0
        TestGraph.AddVertex(1)          # добавляем вершину 1
        TestGraph.AddVertex(2)          # добавляем вершину 2
        TestGraph.AddVertex(3)          # добавляем вершину 3
        TestGraph.AddVertex(4)          # добавляем вершину 4
        TestGraph.AddVertex(5)          # добавляем вершину 5
        TestGraph.AddVertex(6)          # добавляем вершину 6
        TestGraph.AddVertex(7)          # добавляем вершину 7
        TestGraph.AddVertex(8)          # добавляем вершину 8

        TestGraph.AddEdge(0, 1)         # Добавляем ребра
        TestGraph.AddEdge(0, 3)
        TestGraph.AddEdge(0, 5)
        TestGraph.AddEdge(2, 3)
        TestGraph.AddEdge(2, 7)
        TestGraph.AddEdge(3, 4)
        TestGraph.AddEdge(3, 7)
        TestGraph.AddEdge(4, 5)
        TestGraph.AddEdge(4, 6)
        TestGraph.AddEdge(5, 6)
        TestGraph.AddEdge(6, 8)

        Way = TestGraph.WeakVertices()

        for index in range(len(Way)):                                   # пробегаем по результату
            self.assertEqual(Test_List1[index], Way[index].Value)       # проверяем правильность работы метода   

        TestGraph.AddEdge(4, 8)         # Добавим ребро 4-8
                                        # теперь образовался треугольник 4-6-8, и вершина 8 должна выйти из ответа
        Test_List2 = [0, 1]             # а итоговый список должен стать таким
        
        Way2 = TestGraph.WeakVertices() # повторный поиск чтоб проверить, как все внутри обнуяется
        
        for index in range(len(Way2)):                                  # пробегаем по результату
            self.assertEqual(Test_List2[index], Way2[index].Value)      # проверяем правильность работы метода   
            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
