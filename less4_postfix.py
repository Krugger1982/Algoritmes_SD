def postfix_math(expression):
    C = expression[::-1]            # Строку необходимо перевернуть
    S = Stack()
    for i in C:
        S.push(i)                 # Преобразование входной строки в стек
    S1 = Stack()
    while S.size() > 0:
        current = S.pop()
        if current.isdigit():
            S1.push(float(current))
        elif current == '+':
            rezult = 0
            while S1.size() > 0:
                rezult += S1.pop()
            S1.push(rezult)
        elif current == '*':
            rezult = 1
            while S1.size() > 0:
                rezult *= S1.pop()
            S1.push(rezult)
        elif current == '-':
            vichitaemoe = S1.pop()
            umenshaemoe = S1.pop()
            rezult = umenshaemoe - vichitaemoe
            S1.push(rezult)  
        elif current == '/':
            delitel = S1.pop()
            delimoe = S1.pop()
            rezult = delimoe / delitel
            S1.push(rezult)        
        elif current == '=':
            return S1.pop()
    return S1.pop()
