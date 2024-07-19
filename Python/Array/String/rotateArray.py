#A solution that uses a pivot point to rotate the list
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k > len(nums):
            k -= len(nums)
        pivot = len(nums) - k
        nums.extend(nums[:pivot])
        del nums[:pivot]

#A solution that transfer the list to a new list then back
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rot_list = []
        while len(nums) < k:
            k = k - len(nums)
        for x in range(len(nums)):
            rot_list.append(nums[x - k])
        nums[:] = rot_list