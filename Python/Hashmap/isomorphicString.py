# Got a little confused on what was where in the hash map but I got it
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        comparison = {}
        for idx,letter in enumerate(s):
            if letter in comparison:
                if comparison[letter] != t[idx]:
                    return False
            elif t[idx] not in comparison.values():
                comparison[letter] = t[idx]
            else:
                return False
        return True