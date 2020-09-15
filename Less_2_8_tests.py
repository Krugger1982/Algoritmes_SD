import unittest

class MyTestCase(unittest.TestCase):
    def test_1_Add_Vertex(self):
        TestGraph = SimpleGraph(3)                                                  # создаем пустой граф
        self.assertEqual(TestGraph.vertex.count(1), 0)                              # проверка - вершина  в списке вершин графа отсутствует
        TestGraph.AddVertex(1)                                                      # добавляем вершину 1
        self.assertEqual(TestGraph.vertex[0].Value, 1)                              # проверка - вершина 1 появилась в списке на месте с индексом [0]
        self.assertEqual(TestGraph.vertex.count(None), TestGraph.max_vertex - 1)    # проверка - количество None в списке уменьшилось на 1
        
        self.assertEqual(TestGraph.vertex.count(2), 0)                              # проверка - вершина 2 в списке вершин графа отсутствует        
        TestGraph.AddVertex(2)                                                      # добавляем вершину 2
        self.assertEqual(TestGraph.vertex[1].Value, 2)                              # проверка - вершина 2 появилась в списке на месте с индексом [1]
        self.assertEqual(TestGraph.vertex.count(None), TestGraph.max_vertex - 2)    # проверка - количество None в списке уменьшилось на 1

        self.assertEqual(TestGraph.vertex.count(3), 0)                              # проверка - вершина 3 в списке вершин графа отсутствует
        TestGraph.AddVertex(3)                                                      # добавляем вершину 3
        self.assertEqual(TestGraph.vertex[2].Value, 3)                              # проверка - вершина 3 появилась в списке на месте с индексом [2]
        self.assertEqual(TestGraph.vertex.count(None), TestGraph.max_vertex - 3)    # проверка - количество None в списке уменьшилось на 1

    def test_2_IsEdge_and_AddEdge(self):
        TestGraph = SimpleGraph(3)                                                  # создаем пустой граф
        TestGraph.AddVertex('Москва')                                               # добавляем вершину "Москва"
        TestGraph.AddVertex('Питер')                                                # добавляем вершину "Питер"
        TestGraph.AddVertex('Мурманск')                                             # добавляем вершину "Мурманск"

        self.assertEqual(TestGraph.vertex[0].Value, 'Москва')                       # проверка - вершина 'Москва' появилась в списке на месте с индексом 0
        self.assertEqual(TestGraph.vertex[1].Value, 'Питер')                        # проверка - вершина 'Питер' появилась в списке на месте с индексом 1
        self.assertEqual(TestGraph.vertex[2].Value, 'Мурманск')                     # проверка - вершина 'Мурманск' появилась в списке на месте с индексом 2

        
        self.assertFalse(TestGraph.IsEdge(0, 1))                                    # проверка - между вершинами "Москва" и "Питер" ребра нет
        self.assertEqual(TestGraph.m_adjacency[0][1], 0)                            # и ручная проверка того же-  в матрице смежности ребра "Москва-Питер" нет
        self.assertEqual(TestGraph.m_adjacency[1][0], 0)                            
        TestGraph.AddEdge(0, 1)                                                 # Вставляем ребро "Москва-Питер"
        self.assertTrue(TestGraph.IsEdge(0, 1))                                     # проверка - появилось ребро между вершинами "Москва" и "Питер" 
        self.assertEqual(TestGraph.m_adjacency[0][1], 1)                            # и ручная проверка того же - по горизонтали
        self.assertEqual(TestGraph.m_adjacency[1][0], 1)                            # и по вертикали

        self.assertFalse(TestGraph.IsEdge(0, 2))                                    # проверка - между вершинами "Москва" и "Мурманск" ребра нет
        self.assertEqual(TestGraph.m_adjacency[0][2], 0)                            # и ручная проверка того же-  в матрице смежности ребра "Мурманск-" нет
        self.assertEqual(TestGraph.m_adjacency[2][0], 0)                            
        TestGraph.AddEdge(0, 2)                                                 # Вставляем ребро "Москва-Мурманск"
        self.assertTrue(TestGraph.IsEdge(0, 2))                                     # проверка - появилось ребро между вершинами "Москва" и "Мурманск" 
        self.assertEqual(TestGraph.m_adjacency[0][2], 1)                            # и ручная проверка того же
        self.assertEqual(TestGraph.m_adjacency[2][0], 1)                            

        self.assertFalse(TestGraph.IsEdge(1, 2))                                    # проверка - между вершинами "Мурманск" и "Питер" ребра нет
        self.assertEqual(TestGraph.m_adjacency[1][2], 0)                            # и ручная проверка того же-  в матрице смежности ребра "Мурманск-Питер" нет
        self.assertEqual(TestGraph.m_adjacency[2][1], 0)                            
        TestGraph.AddEdge(1, 2)                                                 # Вставляем ребро "Мурманск-Питер"
        self.assertTrue(TestGraph.IsEdge(1, 2))                                     # проверка - появилось ребро между вершинами "Мурманск" и "Питер" 
        self.assertEqual(TestGraph.m_adjacency[1][2], 1)                            # и ручная проверка того же
        self.assertEqual(TestGraph.m_adjacency[2][1], 1)                            

        self.assertFalse(TestGraph.IsEdge(2, 2))                                    # проверка - между вершинами "Мурманск" и "Мурманск" ребра нет (кольцевое ребро
        self.assertEqual(TestGraph.m_adjacency[2][2], 0)                            # и ручная проверка того же
        TestGraph.AddEdge(2, 2)                                                 # Вставляем кольцевое ребро "Мурманск-Мурманск"
        self.assertTrue(TestGraph.IsEdge(2, 2))                                     # проверка - появилось ребро между вершинами "Мурманск" и "Мурманск"
        self.assertEqual(TestGraph.m_adjacency[2][2], 1)                            # и ручная проверка того же

    def test_3_RemoveEdge_and_RemoveVertex(self):
        TestGraph = SimpleGraph(5)                                                  # создаем пустой граф
        TestGraph.AddVertex('Москва')                                               # добавляем вершину "Москва"
        TestGraph.AddVertex('Питер')                                                # добавляем вершину "Санкт_Петербург"
        TestGraph.AddVertex('Вологда')                                              # добавляем вершину "Вологда"
        TestGraph.AddVertex('Псков')                                                # добавляем вершину "Псков"        
  
        TestGraph.AddEdge(0, 1)                         # Вставляем ребро "Москва-Санкт_Петербург"
        TestGraph.AddEdge(0, 2)                         # Вставляем ребро "Москва-Вологда"
        TestGraph.AddEdge(1, 2)                         # Вставляем ребро "Санкт_Петербург-Вологда"
        TestGraph.AddEdge(0, 3)                         # Вставляем ребро "Москва-Псков"
        TestGraph.AddEdge(1, 3)                         # Вставляем ребро "Санкт_Петербург-ПСков"
        
        # Получится такая карта
        #
        #             Вологда(2)           
        #            /          \
        #       СПб(1)    -    Москва(0)
        #             \         /
        #               Псков(3)
        #                               None(4)
        #
        # Матрица смежности будет выгдядеть так:
        #             М СПб В  П  N
        #            (0)(1)(2)(3)(4)
        # Москва (0)  0  1  1  1  0
        # СПб    (1)  1  0  1  1  0
        # Вологда(2)  1  1  0  0  0
        # Псков  (3)  1  1  0  0  0
        # None   (4)  0  0  0  0  0

        TestGraph.RemoveEdge(0, 1)                                              # Удалим ребро "Москва-Санкт_Петербург"
        self.assertFalse(TestGraph.IsEdge(0, 1))                                # проверка - между вершинами "Москва" и "Санкт_Петербург" ребро исчезло
        self.assertEqual(TestGraph.m_adjacency[0][1], 0)                        # и ручная проверка того же - в матрице смежности ребра "Москва-Питер" больше нет
        self.assertEqual(TestGraph.m_adjacency[1][0], 0)                        #

        TestGraph.RemoveVertex(1)           # Удаляем вершину "Санкт-Петербург"
        
        # Получится такая карта
        #
        #             Вологда(2)           
        #                 \
        #      None(1)     Москва(0)
        #                  /
        #             Псков(3)
        #                               None(4)
        #
        # теперь матрица смежности будет выгдядеть так:
        #             М  N  В  П  N
        #            (0)(1)(2)(3)(4)
        # Москва (0)  0  0  1  1  0
        # None   (1)  0  0  0  0  0
        # Вологда(2)  1  0  0  0  0
        # Псков  (3)  1  0  0  0  0
        # None   (4)  0  0  0  0  0
        
        self.assertEqual(TestGraph.vertex[1], None)             # проверка - вместо вершины СПб в списке хранится None
        self.assertEqual(TestGraph.m_adjacency[1][0], 0)                        
        self.assertEqual(TestGraph.m_adjacency[1][1], 0)                        
        self.assertEqual(TestGraph.m_adjacency[1][2], 0)                        
        self.assertEqual(TestGraph.m_adjacency[1][3], 0)                        
        self.assertEqual(TestGraph.m_adjacency[0][1], 0)                        
        self.assertEqual(TestGraph.m_adjacency[2][1], 0)                        
        self.assertEqual(TestGraph.m_adjacency[3][1], 0)        # и исчезли все ребра связанные с вершиной [1]
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
