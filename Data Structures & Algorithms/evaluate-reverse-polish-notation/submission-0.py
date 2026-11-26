class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # if the current token is not an operator
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                # if current token is an operator 
                right = stack.pop()
                left = stack.pop()
    
                if token == "+":
                    stack.append(left + right)
                if token == "-":
                    stack.append(left - right)
                if token == "*":
                    stack.append(left * right)
                if token == "/":
                    stack.append(int(left / right))

        return stack.pop()