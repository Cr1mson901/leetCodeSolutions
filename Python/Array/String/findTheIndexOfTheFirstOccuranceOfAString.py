class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            counter = 0
            answer = 0
            i = 0
            while i < len(haystack):
                if haystack[i] == needle[counter]:
                    counter += 1
                    if counter == len(needle):
                        return answer
                    i += 1
                else:
                    counter = 0
                    i = answer + 1
                    answer = i
        else:
            return -1
# A much simpilar solution when I think about it
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1