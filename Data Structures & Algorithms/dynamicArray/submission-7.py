class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
        


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n



    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array.insert((self.size), n)
        self.size += 1

    def popback(self) -> int:
        return_value = self.array[(self.size-1)]
        self.size -= 1      
        self.array.pop((self.size ))
           
        return return_value

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]

        print(new_array)
        self.array = new_array




    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
