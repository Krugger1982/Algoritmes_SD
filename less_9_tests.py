import unittest

class MyTestCase(unittest.TestCase):

    def test_put_and_get(self):
        list1 = ['Командир', 'старпом', 'штурман', 'боцман', 'механик', 'радист', 'матрос1', 'матрос2']
        list2 = ['Арбузов', 'Букашкин', 'Ведищев', 'Глаголькин', 'Добрый', 'Ершов', 'Живетский', 'Земелин']
        Ex = NativeDictionary(len(list1) * 2)
        for i in range(len(list1)):
            Ex.put(list1[i], list2[i])                      # Создаем тестовый словарь в виде штатного списка экипажа судна
        for i in range(len(list1)):
            self.assertEqual(list2[i], Ex.get(list1[i]))    # Проверка что все правильно записалось
            
    def test_put_exist_key(self):
        list1 = ['Командир', 'старпом', 'штурман', 'боцман', 'механик', 'радист', 'матрос1', 'матрос2']
        list2 = ['Арбузов', 'Букашкин', 'Ведищев', 'Глаголькин', 'Добрый', 'Ершов', 'Живетский', 'Земелин']
        Ex = NativeDictionary(len(list1) * 2)
        for i in range(len(list1)):
            Ex.put(list1[i], list2[i])                      # Создаем тестовый словарь в виде штатного списка экипажа судна
        list1.append('матрос1')
        list2.append('Пупкин')
        Ex.put('матрос1', 'Пупкин')                         # Добавляем по уже существующему ключу новый элемент.
        for i in range(Ex.size):
            if Ex.slots[i] is not None and list1.count(Ex.slots[i]) > 1:
                ind_key = list1.index(Ex.slots[i])
                ind_val = list2.index(Ex.values[i])
                self.assertTrue(list2[ind_key] == Ex.values[i] or list1[ind_val] == Ex.slots[i])    # при совпадении ключа проверяем равенство по переменной value                      

    def test_is_key(self):
        list1 = ['Командир', 'старпом', 'штурман', 'боцман', 'механик', 'радист', 'матрос1', 'матрос2']
        list2 = ['Арбузов', 'Букашкин', 'Ведищев', 'Глаголькин', 'Добрый', 'Ершов', 'Живетский', 'Земелин']
        Ex = NativeDictionary(len(list1) * 2)
        for i in range(len(list1)):
            Ex.put(list1[i], list2[i])                      # Создаем тестовый словарь в виде штатного списка экипажа судна
        for i in list1:
            self.assertNotEqual(Ex.is_key(i), None)         # проверка наличия существующих ключей
        self.assertNotEqual(Ex.is_key('сухопутный'), None)  # проверка отсутствия несуществующего ключа

        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
