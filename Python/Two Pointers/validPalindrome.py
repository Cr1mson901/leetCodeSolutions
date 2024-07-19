class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [letter.lower() for letter in s if letter.isalpha() or letter.isdigit()]
        for x in range(int(len(letters)/2)):
            if letters[x] != letters[-x-1]:
                return False
        return True