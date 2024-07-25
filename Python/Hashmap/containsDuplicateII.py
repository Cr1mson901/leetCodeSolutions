# Easy solution but not that fast
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = {}
        for idx, num in enumerate(nums):
            if num in my_map and idx - my_map[num] <= k:
                return True
            else:
                my_map[num] = idx
        return False
# Apparently enumerate is slightly slower
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = {}
        for i in range(len(nums)):
            if nums[i] in my_map and i - my_map[nums[i]] <= k:
                return True
            else:
                my_map[nums[i]] = i
        return False