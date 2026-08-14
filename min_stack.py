class Min:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self , item):
        if len(self.items) == 0:
            self.items.append([item , item])
        mini = min(self.items[-1][1] , item)
        self.items.append([item , mini])
    def getmin(self):
        if self.is_empty():
            return "Stack is empty"
        print(self.items[-1][1])
    def top(self):
        print(self.items[-1][0])
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        self.items.pop()


find_min = Min()
find_min.push(10)
find_min.push(20)
find_min.push(30)
find_min.getmin()

    

