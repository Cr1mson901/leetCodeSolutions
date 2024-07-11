class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for number in nums:
            if nums.count(number) > 2:
                for i in range(nums.count(number) - 2):
                    nums.remove(number)