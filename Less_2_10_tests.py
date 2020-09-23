import unittest

class MyTestCase(unittest.TestCase):
    def test_1_Simple_Way(self):
        # Создадим тестовый граф
        #       (0) ---(1)  
 
        # Вершины расположены в списке по номерам:
        # [0, 1]
        # Результатом поиска должен стать такой список:
        Test_List = [0, 1]
        
        TestGraph = SimpleGraph(5)      # создаем пустой граф
        TestGraph.AddVertex(0)          # добавляем вершину 0
        TestGraph.AddVertex(1)          # добавляем вершину 1


        TestGraph.AddEdge(0, 1)         # Добавляем ребро


        Way = TestGraph.DepthFirstSearch(0, 1)

        for index in range(len(Way)):
            self.assertEqual(Test_List[index], Way[index].Value)
            
    def test_2_No_Way(self):
        # Создадим тестовый граф
        #       (0) ---(1)  
        #       /  \       \    
        #      /    (3) -- (2)
        #     /    /  \    /
        #   (5)--(4)   \  /
        #      \  |     (7)
        #       \ |       
        #        (6)     (8)
        # Вершины расположены в списке по номерам:
        # TestGraph.vertex == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # Поиск будет вестись, очевидно, в порядке возрастания номеров
        # Результатом поиска должен стать пустой список:
        
        TestGraph = SimpleGraph(9)      # создаем пустой граф
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
        TestGraph.AddEdge(1, 2)
        TestGraph.AddEdge(2, 3)
        TestGraph.AddEdge(2, 7)
        TestGraph.AddEdge(3, 4)
        TestGraph.AddEdge(3, 7)
        TestGraph.AddEdge(4, 5)
        TestGraph.AddEdge(4, 6)
        TestGraph.AddEdge(5, 6)

        self.assertEqual(TestGraph.DepthFirstSearch(0, 8), [])   # проверка, результат - пустой список

    def test_3_Is_Way(self):
        # Создадим тестовый граф
        #       (0) ---(1)  
        #       /  \       \    
        #      /    (3) -- (2)
        #     /    /  \    /
        #   (5)--(4)   \  /
        #      \  |     (7)
        #       \ |      |
        #        (6) -- (8)
        # Вершины расположены в списке по номерам:
        # [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # Поиск будет вестись очевидно, в порядке возрастания номеров
        # Результатом поиска должен стать такой список:
        Test_List = [0, 1, 2, 3, 4, 5, 6, 8]
        
        TestGraph = SimpleGraph(9)      # создаем пустой граф
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
        TestGraph.AddEdge(1, 2)
        TestGraph.AddEdge(2, 3)
        TestGraph.AddEdge(2, 7)
        TestGraph.AddEdge(3, 4)
        TestGraph.AddEdge(3, 7)
        TestGraph.AddEdge(4, 5)
        TestGraph.AddEdge(4, 6)
        TestGraph.AddEdge(5, 6)
        TestGraph.AddEdge(6, 8)
        TestGraph.AddEdge(7, 8)

        Way = TestGraph.DepthFirstSearch(0, 8)

        for index in range(len(Way)):                               # пробегаем по результату
            self.assertEqual(Test_List[index], Way[index].Value)    # проверяем последовательность шагов

        
    def test_4_Is_Way_2(self):
        # Создадим тестовый граф
        #       (0) ---(1)  
        #       /  \           
        #      /    (3) -- (2)
        #     /    /  \    /
        #   (5)--(4)   \  /
        #      \  |     (7)
        #       \ |      
        #        (6) -- (8)
        # Вершины расположены в списке по номерам:
        # [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # тогда верщины 1, 2 и 7 будут отброшены как тупиковые
        # Результатом поиска должен стать такой список:
        Test_List = [0, 3, 4, 5, 6, 8]
        
        TestGraph = SimpleGraph(9)      # создаем пустой граф
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

        Way = TestGraph.DepthFirstSearch(0, 8)

        for index in range(len(Way)):                               # пробегаем по результату
            self.assertEqual(Test_List[index], Way[index].Value)    # проверяем последовательность шагов   
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
