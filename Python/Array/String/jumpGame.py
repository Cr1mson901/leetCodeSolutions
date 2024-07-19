class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:return True
        nums.pop()
        energy = nums[0]
        for num in nums:
            if num > energy:
                energy = num
            if energy == 0:
                return False
            energy -= 1
        return True