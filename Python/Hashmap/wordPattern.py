# I was being dumb and comparing to len(s)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        comparison = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for idx,letter in enumerate(pattern):
            if letter in comparison:
                if comparison[letter] != words[idx]:
                    return False
            elif words[idx] not in comparison.values():
                comparison[letter] = words[idx]
            else:
                return False
        return True