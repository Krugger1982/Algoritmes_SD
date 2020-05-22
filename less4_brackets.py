def Brackets(string):
    br = Stack()
    for i in range(len(string)):
        target = 1
        if string[i] == '(':
            br.push(1)
        elif string[i] == ')':
            target = br.pop()
        if target == None:
            return False
    return br.size() == 0
