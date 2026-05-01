class Solution:

    def __init__(self):

        self.visited = []


    def isHappy(self, n: int) -> bool:

        while n != 1:
            string_n = str(n)

            sum_val = 0
            for digit in string_n:
                sum_val += (int(digit) ** 2)

            if sum_val in self.visited:
                return False

            print(sum_val)

            self.visited.append(sum_val)
            n = sum_val

        return True
            

            
