# An average solution through and through
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}
        for letter in s:
            frequency[letter] = frequency.get(letter,0) + 1
        for letter in t:
            if letter in frequency:
                frequency[letter] -= 1
            else:
                return False
        return all(dif == 0 for dif in frequency.values())