class Solution:

    # initialize stack
    # iterate through each element in tokens
    # if token is an operand, store in stack
    # if is operator, perform operation in first 2 elements in stack

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        operators = ["+", "-", "*", "/"]
        while i < len(tokens):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else: # is an operator
                operator = tokens[i]                    
                operand = stack.pop()
                result = stack.pop()

                if operator == "+":
                        result += operand
                elif operator == "-":
                        result -= operand
                elif operator == "*":
                        result *= operand
                elif operator == "/":
                        result = int(result/operand)
                
                stack.append(result)
            i+=1
        
        return stack.pop()