# Closer but I despise double negatives
class Solution:
    def calculate(self, s: str) -> int:
        numbers = [x for x in s if x!=" "]
        operators = {"+":int.__add__,"-":int.__sub__,"(":0,")":0}
        op_stack = []
        stack = []
        output = [0]
        i = 0
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
        if stack[0] == "-":
            stack[1] *= -1
            del stack[0]
        for i in range(len(stack)):
            if stack[i] in operators.keys():
                num2 = output.pop()
                num1 = output.pop()
                output.append(int(operators[stack[i]](num1,num2)))
            else:
                output.append(int(stack[i]))
        return output[-1]

print(Solution.calculate(Solution, "1-(     -2)"))