# Breaking early is not worth checking after every letter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        frequency = {}
        for letter in ransomNote:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
        for letter in magazine:
            if letter in ransomNote:
                frequency[letter] -= 1
        if all(0 >= amount for amount in frequency.values()):
            return True
        else:
            return False
# Cycle through the smaller list you twat
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        frequency = {}
        for letter in ransomNote:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
        for letter in frequency:
            if frequency[letter] > magazine.count(letter):
                return False
        return True
