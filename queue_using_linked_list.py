class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None

class QueueUsingLL:

    def __init__(self):
       self.head = None
       self.tail = None

    def is_empty(self):
        if self.head == None:
            return False

    def enqueue(self , data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    
    def dequeue(self):
        if self.head.next == None:
            self.head = None
            self.tail = None
        self.head = self.head.next

    def front(self):
        print(self.head.data)

    def rear(self):
        print(self.tail.data)


queue = QueueUsingLL()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.front()

    
    


        

        
        
