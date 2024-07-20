#Very slow but memory efficient
class Solution:
    def maxArea(self, height: List[int]) -> int:
        wall = 0
        max = 0
        for i in range(len(height)):
            if height[i] <= wall:
                continue
            if height[i] * (len(height)-i-1) <= max:
                continue
            for j in range(len(height)-1,i,-1):
                water = min(height[i],height[j]) * (j-i)
                if water > max:
                    max = water
                    wall = height[i]
                if height[i] <= height[j]:
                    break
        return max
# 2 Pointer solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_idx = 0
        r_idx = len(height) - 1
        water = min(height[l_idx], height[r_idx]) * (r_idx - l_idx)
        while l_idx < r_idx:
            if height[l_idx] < height[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
            water = max(water, min(height[l_idx], height[r_idx]) * (r_idx - l_idx))
        return water
