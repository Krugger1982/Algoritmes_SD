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

    def peek(self):
        return self.stack[0]
