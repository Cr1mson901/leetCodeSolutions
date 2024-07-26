# Lord save me for line 10
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+':int.__add__,'-':int.__sub__,'*':int.__mul__,'/':int.__truediv__}
        for i in range(len(tokens)):
            if tokens[i] in operators.keys():
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(str(operators[tokens[i]](num1,num2)).split(".")[0]))
            else:
                stack.append(int(tokens[i]))
        return stack[0]