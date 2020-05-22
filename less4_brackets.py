def Brackets(string):
    br = Stack()
    for i in range(len(string)):
        try:
            if string[i] == '(':
                br.push(1)
            elif string[i] == ')':
                br.pop()
        except IndexError:
            return False
    return br.size() == 0
