class MinStack:

    def __init__(self):
        self.minimum = float('inf')
        self.stack = []
        self.min_stack = []

        

    def push(self, val: int) -> None:
        if val <= self.minimum:
            self.minimum = val
            self.min_stack.append(self.minimum)

        self.stack.append(val)
        
        

    def pop(self) -> None:
        if (self.stack[-1]) == self.minimum:
        
            self.min_stack.pop()
            if len(self.min_stack) == 0:
                self.minimum = float('inf')
                
            else:
                self.minimum = self.min_stack[-1]
                

        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
