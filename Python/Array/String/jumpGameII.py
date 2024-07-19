#A far more complicated solution that can be cleaned up
class Solution:
    def jump(self,nums) -> int:
        if len(nums) < 2:return 0
        if nums[0] >= len(nums) - 1: return 1
        if len(nums) == 3: return 2
        jumps = 1
        finish_line = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= finish_line:
                del nums[i+1:]
                jumps = 1
            elif jumps == 1:
                nums[i] = 1
                jumps = 2
            elif nums[i] > nums[i+1]:
                removed = 1
                while nums[i] > nums[i + 1]:
                    nums[i] -= nums[i+1]
                    removed += nums[i+1]
                    del nums[i+1]
                nums[i] = removed
            else: nums[i] = 1
            finish_line += 1
            jumps += 1
        return len(nums)

#A slow solution that goes over the list multiple times
class Solution:
    def jump(self, nums) -> int:
        if len(nums) < 2:return 0
        if nums[0] >= len(nums) - 1: return 1
        jumps = 0
        while len(nums) > 1:
            nums.pop()
            finish_line = 1
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] >= finish_line:
                    del nums[i+1:]
                finish_line += 1
            jumps += 1
        return jumps