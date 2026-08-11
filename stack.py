class Stack:
    def __init__(self):
        self.items = [] # defining list 

    def is_empty(self): # checking if empty 
        return len(self.items) == 0
    
    def push(self , item):  # pusing
        self.items.append(item)

    def pop(self): # popping
        if self.is_empty():
            return "cannot pop , stack is empty"
        x = self.items.pop()
        return x
    
    def top(self): # returning top element
        if self.is_empty():
            return "Cannot top , stack is empty"
        return self.items[-1]
    
    def size(self): # returning size
        return len(self.items)
    
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.top())