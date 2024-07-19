class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [number for number in nums if number != val]
        return len(nums)