# Solved in a minute. Easy Peasy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        math = {}
        for i in range(len(nums)):
            if nums[i] in math.keys():
                return [math[nums[i]],i]
            else:
                math[target-nums[i]] = i