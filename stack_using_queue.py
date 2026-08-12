from collections import deque
class StackUsingQueue:
    def is_empty(self):
        return len(self.queue) == 0
    def __init__(self):
        self.queue = deque()
    def push(self , item):
        self.queue.append(item)
        for _ in range(len(self.queue) -1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        x = self.queue.popleft()
        return f"Popped element{x}"
    def peek(self):
        if self.is_empty():
            return "Stakc is empty"
        return self.queue[0]
    def size(self):
        return len(self.queue)

stack = StackUsingQueue()
stack.push(100)
stack.push(200)
stack.push(300)
print(stack.size())
    
    
        
