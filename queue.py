class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self ,item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "queue is empty , cannot pop"
        self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Cannot peek , queue is empty"
        print(self.items[0])

    def rear(self):
        if self.is_empty():
            return "Cannot rear no element"
        print(self.items[-1])

    def size(self):
        print(len(self.items))

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.rear()
