#The most convuluted way to solve this but it works now so I am happy
class Solution:
    def calculate(self, s: str) -> int:
        numbers = [x for x in s if x!=" "]
        operators = {"+":int.__add__,"-":int.__sub__,"(":0,")":0}
        op_stack = []
        stack = []
        output = [0]
        i = 0
        #Checks for negative numbers
        for n in range(len(numbers)):
            if numbers[n] == '-':
                try:
                    if numbers[n-1] == '(':
                        raise Exception('Negative')
                except:
                    numbers.insert(n,'0')
        # Converts to Reverse Polish Notation
        while i < len(numbers):
            if numbers[i] not in operators:
                j = i + 1
                while j < len(numbers) and numbers[j] not in operators:
                    j += 1
                stack.append(int("".join(numbers[i:j])))
                i = j
                continue
            elif numbers[i] == "(":
                op_stack.append(numbers[i])
            elif numbers[i] == ")":
                while op_stack[-1] != "(":
                    stack.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and (op_stack[-1] == "-" or op_stack[-1] == "+"):
                    stack.append(op_stack.pop())
                op_stack.append(numbers[i])
            i += 1
        while op_stack:
            stack.append(op_stack.pop())
        #Calculates based on RPN
        for i in range(len(stack)):
            if stack[i] in operators.keys():
                num2 = output.pop()
                num1 = output.pop()
                output.append(int(operators[stack[i]](num1,num2)))
            else:
                output.append(int(stack[i]))
        return output[-1]