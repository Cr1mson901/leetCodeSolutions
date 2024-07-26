# Happy with this solution
class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = [word for word in path.split("/") if word != "" and word != "."]
        stack = []
        path = "/"
        for i in range(len(elements)):
            if elements[i] != "..":
                stack.append(elements[i])
            elif len(stack) > 0:
                stack.pop()
        path += path.join(stack)
        return path