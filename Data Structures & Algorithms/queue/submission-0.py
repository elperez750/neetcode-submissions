class QueueNode:

    def __init__(self, value, next=None, prev=None):
        self.value = value 
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0



    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        newNode = QueueNode(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        self.length += 1
        
            

    def appendleft(self, value: int) -> None:
        newNode = QueueNode(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode


        self.length += 1

        

    def pop(self) -> int:
        value_to_return = self.tail

        if self.isEmpty():
            return -1

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1
        return value_to_return.value

        
        

    def popleft(self) -> int:

        value_to_return = self.head

        if self.isEmpty():
            return -1

        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.next
            self.head.prev = None

        
        self.length -= 1
        return value_to_return.value
        
