class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None

class StackUsingLL:

    def __init__(self):
       self.head = None
       self.tail = None

    def is_empty(self):
        if self.head == None:
            return False

    def push(self , data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    
    def pop(self):
        if self.head.next == None:
            self.head = None
            self.tail = None
        self.tail = self.tail.prev

    def peek(self):
        print(self.tail.data)


stack = StackUsingLL()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.peek()

    
    


        

        
        
