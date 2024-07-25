# This is what I came up with but it is too slow
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_map = {}
        output = 0
        for i in range(len(nums)):
            if nums[i] in my_map.keys():
                continue
            start = nums[i]
            end = nums[i] + 1
            if end not in my_map.keys() and start not in my_map.values():
                my_map[start] = end
                continue
            while end in my_map.keys():
                my_map[start] = my_map[end]
                del my_map[end]
                end = my_map[start]
            while start in my_map.values():
                start2 = list({j for j in my_map.keys() if my_map[j] == start})[0]
                my_map[start2] = end
                try:
                    del my_map[start]
                except:
                    pass
                start = start
        for start,end in my_map.items():
            if end - start > output:
                output = end - start
        return output

# A much simpilar solution then what I was trying. Searching algorithms are faster then I thought
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_map = {0:0}
        nums = set(nums)
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                i = 1
                my_map[num] = 1
                while num + i in nums:
                    my_map[num] += 1
                    i += 1
        return max(my_map.values())