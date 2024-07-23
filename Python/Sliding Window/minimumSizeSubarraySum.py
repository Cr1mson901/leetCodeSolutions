# O(N) but slow
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        window = []
        count = 0
        size = float('inf')
        for i in range(len(nums)):
            window.append(nums[i])
            count += nums[i]
            while count - window[0] >= target:
                count -= window[0]
                del window[0]
            if count >= target and len(window) < size:
                size = len(window)
        return size
# Same concept I just need to stop using a list as the window and instead use two pointers
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        left = 0
        sum_of_window = 0
        size = float('inf')
        for right in range(0,len(nums)):
            sum_of_window += nums[right]
            while sum_of_window >= target:
                size = min(size,(right-left+1))
                sum_of_window -= nums[left]
                left += 1
        return size
