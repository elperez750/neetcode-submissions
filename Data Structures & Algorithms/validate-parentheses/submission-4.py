class Solution:
    def isValid(self, s: str) -> bool:
        complement = {"]" : "[", ")":"(", "}": "{" }
        if (len(s) % 2) != 0:
            return False


        stack = []
        for char in s:
            if char in complement.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                if complement[char] == stack[-1]:
                    stack.pop()

                else:
                    return False
              

        return len(stack) == 0