import unittest

class MyTestCase(unittest.TestCase):

    def test_put_and_get_and_getHits(self):
        list1 = ['Командир', 'старпом', 'штурман', 'боцман', 'механик', 'радист', 'матрос1', 'матрос2']
        list2 = ['Арбузов', 'Букашкин', 'Ведищев', 'Глаголькин', 'Добрый', 'Ершов', 'Живетский', 'Земелин']
        Ex = NativeCache(len(list1))
        for i in range(len(list1)):
            Ex.put(list1[i], list2[i])                      # Создаем тестовый словарь в виде штатного списка экипажа судна
        for i in range(len(list1)):
            self.assertEqual(Ex.get_hits(list1[i]), 0)      # Проверка изначального состояния счетиков обращений
            self.assertEqual(list2[i], Ex.get(list1[i]))    # Проверка что все правильно записалось
            self.assertEqual(Ex.get_hits(list1[i]), 1)      # Проверка изменившегося состояния счетчиков обращений
        
            
    def test_put_exist_key(self):
        list1 = ['Командир', 'старпом', 'штурман', 'боцман', 'механик', 'радист', 'матрос1', 'матрос2']
        list2 = ['Арбузов', 'Букашкин', 'Ведищев', 'Глаголькин', 'Добрый', 'Ершов', 'Живетский', 'Земелин']
        Ex = NativeCache(len(list1))
        for i in range(len(list1)):
            Ex.put(list1[i], list2[i])                          # Создаем тестовый словарь в виде штатного списка экипажа судна
        for i in range(len(list1)):
            self.assertEqual(list2[i], Ex.get(list1[i]))        # Проверка что все правильно записалось, попутно даем по 1 обращению к каждому элементу
        for i in range(len(list1)-1):                           # Обращаемся ко всем кроме элемента "матрос2"
            self.assertEqual(list2[i], Ex.get(list1[i]))
            self.assertEqual(Ex.get_hits(list1[i]), 2)          # Проверка изменившегося состояния счетчиков обращений
            self.assertEqual(Ex.get_hits(list1[len(list1)-1]), 1)       # Проверка состояния счетчика обращений элемента "матрос2" (не изменилось)
        Ex.put('матрос2', 'Ижицин')                                     # Добавляем по уже существующему ключу новый элемент.
        self.assertEqual('Ижицин', Ex.get('матрос2'))           # Проверяем что он вставился в ожидаемую позицию ("матрос2" перезаписадся)
        for i in range(len(list1)-1):                           # Обращаемся ко всем кроме элемента "матрос2"
            self.assertEqual(list2[i], Ex.get(list1[i]))
            self.assertEqual(Ex.get_hits(list1[i]), 3)                  # Проверка изменившегося состояния счетчиков обращений
            self.assertEqual(Ex.get_hits(list1[len(list1)-1]), 2)       # Проверка состояния счетчика обращений элемента "матрос2" (не изменилось)
        Ex.put('матрос3', 'Нашенский')                          # Добавляем еще один элемент
        self.assertEqual('Нашенский', Ex.get('матрос3'))        # Проверяем что он вставился
        self.assertFalse(Ex.is_key('матрос2'))                  # проверка что ключ "матрос2" исчез ("матрос3" вставился на его место)
        
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
