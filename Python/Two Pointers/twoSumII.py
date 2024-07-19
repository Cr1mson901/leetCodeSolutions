#Not good code. Almost timed out
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)-1,i,-1):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                elif numbers[i] + numbers[j] < target:
                    break
#Faster but not god enough
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)-1,i,-1):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                elif numbers[i] + numbers[j] < target:
                    break
                else:
                    numbers.pop()
# Added list comprehension
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = [num for num in numbers if num + numbers[0] <= target]
        for i in range(len(numbers)):
            for j in range(len(numbers)-1,i,-1):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                elif numbers[i] + numbers[j] < target:
                    break
                else:
                    numbers.pop()