class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()

        self.array[self.getSize()] = n
        self.size += 1
        


    def popback(self) -> int:
        size = self.getSize()
        if size == 0:
            raise IndexError("Cannot pop from an empty array")
        value = self.array[size-1]
        self.array[size-1] = None
        self.size -= 1
        return value

 

    def resize(self) -> None:
        self.capacity *= 2
        self.array = self.array + ([None] * (self.capacity // 2))


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity