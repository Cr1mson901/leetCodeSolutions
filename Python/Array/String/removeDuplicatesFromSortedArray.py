class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = set(nums)
        nums[:] = list(nums)
        nums.sort()
        return len(nums)