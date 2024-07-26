# Too many ifs for my liking
class Solution:
    def isValid(self, s: str) -> bool:
        waiting = []
        starts = {"(":")","{":"}","[":"]"}
        for bracket in s:
            if bracket in starts:
                waiting.append(starts[bracket])
            elif len(waiting) == 0:
                return False
            elif bracket == waiting[-1]:
                waiting.pop()
            else:
                return False
        if len(waiting) == 0:
            return True
        else:
            return False
#Use the len comparison as the return and check against the pop directly
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starts = {"(":")","{":"}","[":"]"}
        for bracket in s:
            if bracket in starts:
                stack.append(starts[bracket])
            elif len(stack) == 0 or bracket!=stack.pop():
                return False
        return len(stack) == 0