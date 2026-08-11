class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self ,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "queue is empty , cannot pop"
        self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Cannot peek , queue is empty"
        print(self.items[0])

    def size(self):
        print(len(self.items))

queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.peek()
queue.size()

    