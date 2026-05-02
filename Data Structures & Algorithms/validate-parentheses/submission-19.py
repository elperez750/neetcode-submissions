class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        if len(s) == 1:
            return False

        stack = ["#"]
        for char in s:
            if char in mapping and stack[-1] == mapping[char]:
                stack.pop()
           
            else:
                stack.append(char)
          

        return len(stack) == 1