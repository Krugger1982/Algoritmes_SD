class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        x = None
        try:
            x = self.stack[0]
            del self.stack[0]
        except IndexError:
            pass
        return x     
    
    def push(self, value):
        self.stack.insert (0, value)

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if  self.s2.size() == 0:
            while self.s1.size() > 0:
                self.s2.push(self.s1.pop())
        return self.s2.pop() 

    def size(self):
        return self.s1.size() + self.s2.size()
