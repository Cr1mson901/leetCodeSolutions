class Solution:
    def trap(self, height: List[int]) -> int:
        wall = height[0]
        wall_x = 0
        water = 0
        total = 0
        for i in range(0,len(height)):
            if height[i] < wall and i != len(height)-1:
                water += wall - height[i]
            elif height[i] >= wall:
                total += water
                water = 0
                wall = height[i]
                wall_x = i
            else:
                water = 0
                wall = height[-1]
                for i in range(len(height)-2,wall_x -1,-1):
                    if height[i] < wall:
                        water += wall - height[i]
                    elif height[i] >= wall:
                        total += water
                        water = 0
                        wall = height[i]
        return total