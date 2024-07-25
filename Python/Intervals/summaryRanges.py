# Fine
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        my_range = []
        i = 0 
        while i < len(nums):
            start = nums[i]
            if nums[i] + 1 not in nums:
                my_range.append(str(start))
                i += 1
                continue
            while nums[i] + 1 in nums:
                i += 1
            my_range.append(f"{start}->{nums[i]}")
            i += 1
        return my_range

# Better on memory but not much faster.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        my_range = []
        i = 0 
        while i < len(nums):
            j = 1
            start = nums[i]
            while i + j < len(nums) and nums[i] + j == nums[i+j]:
                j += 1
            if 1 == j:
                my_range.append(str(start))
                i += 1
                continue
            else:
                my_range.append(f"{start}->{nums[i+j-1]}")
            i = j + i
        return my_range