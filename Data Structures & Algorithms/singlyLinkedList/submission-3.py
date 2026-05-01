class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        curr = self.head
        place = 0
        while curr:
            if place == index:
                return curr.value
            place += 1
            curr = curr.next
        return -1
            


        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.tail = new_node
        else:

            new_node.next = self.head
            
        self.head = new_node
        print(new_node.value)
        
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def remove(self, index: int) -> bool:
        if index == 0:
            if not self.head:
                return False
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True


        curr = self.head
        count = 0
        while curr and curr.next:
            if count == (index - 1):

                curr.next = curr.next.next
                if not curr.next:
                    self.tail = curr

                return True
            
            count += 1
            curr = curr.next

        return False
                
        

            
        

    def getValues(self) -> List[int]:
        linked_list_values = []
        curr = self.head
        while curr:
            print(curr.value)
            linked_list_values.append(curr.value)
            curr = curr.next
            

        return linked_list_values
        
