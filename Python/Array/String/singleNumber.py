# List comprehension one liner
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [answer for answer in set(nums) if nums.count(answer) == 1][0]
    
# Xor operator. Since every number appears twice except for one. The numbers will cancel out and leave only the answer
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer