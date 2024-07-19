class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if " " in s:
            test = s.split(" ")
        else:
            return len(s)
        for i in range(1,len(test) + 1):
            if len(test[-i]) > 0:
                return len(test[-i])