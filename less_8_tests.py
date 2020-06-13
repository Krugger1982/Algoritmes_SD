import unittest

class MyTestCase(unittest.TestCase):

    def test_find(self):
        list1 = ['Привет', 'я', 'Урфин', 'Джюс', 'и', 'это', 'мои', 'деревянные солдаты']
        Exindexes = [0, 7, 4, 1, 3, 5, 2, 6]        # так распределятся их индексы в проверяемой хэштаблице
        Ex = HashTable(len(list1), 3)
        for i in list1:
            Ex.put(i)                               # создаем и заполняем тестовую хэштаблицу
        for i in range(len(list1)):
            self.assertEqual(Ex.find(list1[i]), Exindexes[i])   # проверка - поиск имеющихся элементов
        self.assertEqual(Ex.find('всемогущие'), None)           # проверка - поиск отсутствующего жлемента

    def test_hashFun_and_find(self):
        list1 = ['Привет', 'я', 'Урфин', 'Джюс', 'и', 'это', 'мои', 'деревянные солдаты']
        Ex = HashTable(len(list1), 3)
        for i in list1:
            Ex.put(i)                           # создаем и заполняем тестовую хэштаблицу
        for i in list1:
            HF = 0
            for j in i:
                HF += ord(j)
            HF = HF % len(list1)                                    # "ручной" подсчет хэш-функции 
            self.assertEqual(HF, Ex.hash_fun(Ex.slots[Ex.find(i)]))  # сравнение с табличным значением

    def test_put(self):
        list1 = ['Привет', 'я', 'Урфин', 'Джюс', 'и', 'это', 'мои', 'деревянные солдаты']
        Ex = HashTable(len(list1), 3)
        for i in list1:
            Ex.put(i)
        self.assertEqual(Ex.size, len(list1))                
        self.assertEqual(Ex.put('переполнение'), None)      # проверка при переполнении

    def test_seek_slot(self):
        list1 = ['Привет', 'я', 'Урфин', 'Джюс', 'и', 'это', 'мои', 'деревянные солдаты']
        Exindexes = [0, 7, 4, 1, 3, 5, 2, 6]
        Ex = HashTable(len(list1), 3)        
        for i in range(len(list1)):
            self.assertEqual(Ex.seek_slot(list1[i]), Exindexes[i])
            Ex.put(list1[i])
        self.assertEqual(Ex.seek_slot('переполнение'), None)      # проверка при переполнении
                         

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
