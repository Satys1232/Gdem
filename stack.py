class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self , item):
        self.items.append(item)
    def pop(self):
        if self.is_empty:
            return "cannot pop , stack is empty"
        x = self.items.pop()
        return x
    def top(self):
        if self.is_empty:
            return "Cannot top , stack is empty"
        return self.items[-1]
    def size(self):
        return len(self.items)
stack = Stack()
stack.push(10)
stack.push(20)
stack.pop()
stack.pop()
print(stack.pop())