import unittest

class MyTestCase(unittest.TestCase):
    def test_1_MakeHeap(self):
        TestArray = [0, 98, 35, 2, 33, 14, 25, 48, 8, 11]    # создадим тестовый массив неповторяющихся положительных (или 0) целых чисел
        result = [98, 48, 35, 33, 11, 14, 25, 0, 8, 2]       # в куче он должен распределиться так
        #                    98
        #                 /      \
        #               48        35
        #             /    \     /  \
        #          33      11   14   25
        #         /  \    /     
        #        0    8  2  
        #
 
        depth = 0
        Number = 1
        while Number < len(TestArray):                           # определим глубину кучи
            depth += 1
            Number *= 2
        TestHeap = Heap()
        self.assertFalse(TestHeap.Add(TestArray[0]))            # проверка - просто так в пустую кучу элемент не вставишь
                         
        TestHeap.MakeHeap(TestArray, depth)                     # заполняем кучу из массива
        result = [98, 48, 35, 33, 11, 14, 25, 0, 8, 2]
        for i in range(len(TestHeap.HeapArray)):
            self.assertEqual(TestHeap.HeapArray[i], result[i])
        

    def test_3_GetMax_and_add(self):
        TestArray = [0, 98, 35, 2, 33, 14, 25, 48, 8, 11, 3]    # создадим тестовый массив неповторяющихся положительных (или 0) целых чисел
        TestHeap = Heap()
        self.assertEqual(TestHeap.GetMax(), -1)                 # проверка - куча пустая, ничего не удаляется 
        self.assertFalse(TestHeap.Add(TestArray[0]))            # проверка - просто так в пустую кучу элемент не вставишь

        depth = 0
        Number = 1
        while Number < len(TestArray):                           # определим будущую глубину кучи
            depth += 1
            Number *= 2
        TestHeap.MakeHeap(TestArray, depth)                     # заполняем кучу из массива
        result = [98, 48, 35, 33, 11, 14, 25, 0, 8, 2, 3]
        # в куче он должен распределиться так
        #                    98
        #                 /      \0
        #               48        35
        #             /    \     /  \
        #          33      11   14   25
        #         /  \    /  \    
        #        0    8  2    3

        
        self.assertEqual(TestHeap.GetMax(), 98)                 # удалим головной элемент(98)
        # куча изменится
        #                    48
        #                 /      \
        #               33        35
        #             /    \     /  \
        #          8       11   14   25
        #         /  \    /       
        #        0    3  2             
        
        result = [48, 33, 35, 8, 11, 14, 25, 0, 3, 2]
        for i in range(len(TestHeap.HeapArray)):
            self.assertEqual(TestHeap.HeapArray[i], result[i])
            
        self.assertTrue(TestHeap.Add(50))                       # добавим 50 (самый большой ключ)
        # куча изменится
        #                    50
        #                 /      \
        #               48        35
        #             /    \     /  \
        #          8       33   14   25
        #         /  \    /  \     
        #        0    3  2   11         
        
        result = [50, 48, 35, 8, 33, 14, 25, 0, 3, 2, 11]
        for i in range(len(TestHeap.HeapArray)):
            self.assertEqual(TestHeap.HeapArray[i], result[i])        
            
        self.assertTrue(TestHeap.Add(30))                       # добавим 30 (ключ средней длины)
        # куча изменится
        #                       50
        #                  /         \
        #               48            35
        #             /    \         /  \
        #          8       33      30    25
        #         /  \    /  \    / 
        #        0    3  2   11  14    
        
        result = [50, 48, 35, 8, 33, 30, 25, 0, 3, 2, 11, 14]
        for i in range(len(TestHeap.HeapArray)):
            self.assertEqual(TestHeap.HeapArray[i], result[i])             

        self.assertEqual(TestHeap.GetMax(), 50)                 # удалим головной элемент(50)
        # куча изменится
        #                    48
        #                 /      \
        #               33        35
        #             /    \     /  \
        #          8       14   30   25
        #         /  \    /  \     
        #        0    3  2    11         
        
        result = [48, 33, 35, 8, 14, 30, 25,  0, 3, 2, 11]
        for i in range(len(TestHeap.HeapArray)):
            self.assertEqual(TestHeap.HeapArray[i], result[i])

        self.assertTrue(TestHeap.Add(1))                       # добавим 1 (самый маленький ключ)
        self.assertTrue(TestHeap.Add(4))
        self.assertTrue(TestHeap.Add(5))
        self.assertTrue(TestHeap.Add(7))
        # куча изменится
        #                       48
        #                  /         \
        #               33             35
        #             /    \         /    \
        #          8       14       30     25
        #         /  \    /  \     / \    /  \
        #        0    3  2    11  1   4  5    7
        
        result = [48, 33, 35, 8, 14, 30, 25,  0, 3, 2, 11, 1, 4, 5, 7]
        for i in range(len(TestHeap.HeapArray)):
            self.assertEqual(TestHeap.HeapArray[i], result[i])
        self.assertFalse(TestHeap.Add(15))                       # добавим 15 (сверх заданной глубины элемент не вставится)

        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
