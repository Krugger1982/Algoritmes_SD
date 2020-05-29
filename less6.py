class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        x = None
        if len(self.deque) > 0:
            x = self.deque.pop(0)
        return x

    def removeTail(self):
        x = None
        if len(self.deque) > 0:
            x = self.deque.pop()
        return x

    def size(self):
        return len(self.deque)
