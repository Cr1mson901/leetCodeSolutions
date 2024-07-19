class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        if len(s) == 0:
            return True
        for letter in t:
            if letter == s[count]:
                count += 1
            if count == len(s):
                return True
        return False