class Solution:
    def isValid(self, s: str) -> bool:
        complement = {"]" : "[", ")":"(", "}": "{" }
        if (len(s) % 2) != 0:
            return False

        if len(s) == 0:
            return True

        stack = []
        for i in range(len(s)):
            if s[i] in complement.values():
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                if complement[s[i]] == stack[len(stack) -1]:
                    stack.pop()
                else:
                    return False
              

        return len(stack) == 0