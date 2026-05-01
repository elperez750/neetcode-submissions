class MinHeap:
    
    def __init__(self):
        self.heap = [0]


    def push(self, val: int) -> None:
        #appending the value to the bottom of heap
        self.heap.append(val)

        #getting the index for new value
        i = len(self.heap) - 1

        #Percolate up while the new value we inserted is less than its parent. 
        #It would be the opposite in a max heap
     
        while self.heap[i] < self.heap[i // 2] and i // 2 != 0:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp

            i = i // 2

    def helper(self, start, left, right):
        #We first check if the right child exists
        while left < len(self.heap):

            #If it does, we want to compare and see if it is the smallest between the left and the right
            #If it is the smallest, we want to make sure that the root is smaller
            #if the root is not smaller than the right, we check the left
            #if its not smaller than left, we break
            #This is because self.heap[i] would be in the right place
            if (right < len(self.heap)) and (self.heap[right] < self.heap[left]) and (self.heap[start] > self.heap[right]):
                temp = self.heap[start]
                self.heap[start] = self.heap[right]
                self.heap[right] = temp
                start = right
            #if we make it to this case:
            #1: right child did not exist
            #2: right child did exist, but it was bigger than the left child
            elif self.heap[start] > self.heap[left]:
                temp = self.heap[start]
                self.heap[start] = self.heap[left]
                self.heap[left] = temp
                start = left
            else:
                break
            
            left = start * 2
            right = (start * 2) + 1



    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1

        if len(self.heap) == 2:
            return self.heap.pop()

        #creating copy of old root
        old_root = self.heap[1]

        #copying last element to root
        self.heap[1] = self.heap.pop()

        #starting index at root
        i = 1

        self.helper(i, i*2, (i*2) + 1)
        

        return old_root


    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        else:
            return self.heap[1]

    
    def heapify(self, nums: List[int]) -> None:
        
        self.heap += nums
        print(self.heap)
        cur = (len(self.heap)-1) // 2
        start = cur * 2
        end = (cur * 2) + 1
        while cur > 0:
            self.helper(cur, start, end)
            cur -= 1
            start = cur * 2
            end = (cur * 2) + 1

        




        
        