class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try: 
                stack.append(int(token))

            except:
                second_element = stack.pop()
                first_element = stack.pop()
                if token == "+":
                    result = first_element + second_element
                elif token == "-":
                    result = first_element - second_element
                elif token == "*":
                    result = first_element * second_element
                else:
                    result = int(first_element / second_element)

                stack.append(result)
        return stack[0]
    


        