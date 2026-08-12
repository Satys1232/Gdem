class StackQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def is_empty(self):
        return len(self.st1) == 0

    def enqueue(self , x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        self.st1.pop()

    def peek(self):
        if self.is_empty():
            return "queue is empty"
        print(self.st1[-1])
    

queue = StackQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.peek()
print(queue.st1)