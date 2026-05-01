class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0  # Logical size of the array

    def get(self, i: int) -> int:
        if i >= self.size or i < 0:
            raise IndexError("Index out of bounds")
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.size or i < 0:
            raise IndexError("Index out of bounds")
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Cannot pop from an empty array")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return value

    def resize(self) -> None:
        new_array = [None] * (self.capacity * 2)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.capacity *= 2
        self.array = new_array

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
