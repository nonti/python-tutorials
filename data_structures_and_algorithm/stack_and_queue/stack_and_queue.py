class StackQueue:
    def __init__(self):
        self.stack = []
        self.queue = []
        
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)
    
sq = StackQueue()
sq.push(1)
sq.push(2)

sq.enqueue(3)
sq.enqueue(4)

popped_item = sq.pop()
print(popped_item)
dequeued_item = sq.dequeue()
print(dequeued_item)