# Too Slow O(n2)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         total = []
#         temp = 0
#         for i in range(len(nums)):
#             temp = nums.pop(0)
#             temp2 = 1
#             for number in nums:
#                 temp2 *= number
#             total.append(temp2)
#             nums.append(temp)
#         return total
# Also Too Slow 😡
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         total = [1 for x in range(len(nums))]
#         for i in range(len(nums)):
#             total[:] = [temp * nums[i] if i != idx else temp for idx, temp in enumerate(total)]
#         return total
# Uses Memory to get through long sets of repeating values but doesn't actually address the problem
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         total = []
#         memory = {}
#         temp = 0
#         for i in range(len(nums)):
#             temp = nums.pop(0)
#             temp2 = 1
#             if memory.get(temp):
#                 total.append(memory[temp])
#                 nums.append(temp)
#                 continue
#             for number in nums:
#                 temp2 *= number
#             total.append(temp2)
#             nums.append(temp)
#             memory[temp] = temp2
#         return total
# A crackhead solution that I didn't come up with on my own
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        temp = 1
        for i in range(0,len(nums)):
            output.append(temp)
            temp *= nums[i]
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= temp
            temp *= nums[i]
        return output