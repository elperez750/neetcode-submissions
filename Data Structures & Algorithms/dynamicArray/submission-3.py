class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * self.capacity


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()

        self.array[self.getSize()] = n
        


    def popback(self) -> int:
        size = self.getSize()
        if size == 0:
            raise IndexError("Cannot pop from an empty array")
        value = self.array[size-1]
        self.array[size-1] = None
        return value

 

    def resize(self) -> None:
        self.capacity *= 2
        self.array = self.array + ([None] * (self.capacity // 2))


    def getSize(self) -> int:
        count = 0
        for i in range(len(self.array)):
            if self.array[i] is not None:
                count += 1
        return count
        
    
    def getCapacity(self) -> int:
        return self.capacity