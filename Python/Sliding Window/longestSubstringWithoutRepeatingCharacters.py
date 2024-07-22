class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        output = 0
        for letter in s:
            try:
                rmv = substring.index(letter)
                if len(substring) > output:
                    output = len(substring)
                del substring[:rmv+1]
                substring.append(letter)
            except:
                substring.append(letter)
        return max(output, len(substring))