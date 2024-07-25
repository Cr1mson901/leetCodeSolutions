# Easy solution but not that fast
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {}
        for idx, num in enumerate(nums):
            if num in myMap and idx - myMap[num] <= k:
                return True
            else:
                myMap[num] = idx
        return False
# Apparently enumerate is slightly slower
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {}
        for i in range(len(nums)):
            if nums[i] in myMap and i - myMap[nums[i]] <= k:
                return True
            else:
                myMap[nums[i]] = i
        return False