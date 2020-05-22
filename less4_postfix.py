def postfix_math(expression):
    S1 = Stack()
    while expression.size() > 0:
        current = expression.pop()
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
        elif current == '=':
            return S1.pop()
    return S1.pop()
