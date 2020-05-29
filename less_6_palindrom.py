def palindrom(String):
    Ochered = Deque()
    String = ''.join(String.split()).lower()            # Избавляемся от пробелов и приводим всю строку к нижнему регистру
    for i in String:
        Ochered.addTail(i)                              # переписыввем содержание строки в очередь Deque
    while Ochered.size() > 1:
        A = Ochered.removeFront()
        B = Ochered.removeTail()
        if A != B:
            return False
    return True
