class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * capacity


    

    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity


        while True:
            if self.map[index] == None:
                new_value = Pair(key, value)
                self.map[index] = new_value
                self.size += 1
                if (self.size >= self.capacity // 2):
                    self.resize()
                return
            
            elif self.map[index].key == key:
                self.map[index].value = value
                return
            
            index += 1
            index = index % self.capacity


            
    def get(self, key: int) -> int:
        index = key % self.capacity

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            
            index += 1
            index = index % self.capacity

        return -1



    def remove(self, key: int) -> bool:
        index = key % self.capacity

        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            
            index += 1
            index = index % self.capacity
        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity *= 2
        old_map = self.map
        self.map = [None] * self.capacity
        self.size = 0

        for pair in old_map:
            if pair:
                self.insert(pair.key, pair.value)

            
        



