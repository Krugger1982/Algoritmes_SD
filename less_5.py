class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        x = None
        try:
            x = self.queue[0]
            del self.queue[0]
        except IndexError:
            pass
        return x   

    def size(self):
        return len(self.queue)
