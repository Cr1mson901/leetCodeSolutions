class Solution:
    def calculate(self, s: str) -> int:
        numbers = [x for x in s if x!="(" and x!=")" and x!=" "]
        output = []
        function = 1
        operators = ("-","+")
        i = 0
        while i < len(numbers):
            if numbers[i] in operators:
                if numbers[i] == "-":
                    function *= -1
                i += 1
            else:    
                j = i + 1
                while j < len(numbers) and numbers[j] not in operators:
                    j += 1
                output.append(function * int("".join(numbers[i:j])))
                i = j
                function = 1
        return sum(output)