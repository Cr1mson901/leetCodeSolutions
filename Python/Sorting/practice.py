#Hoare Partition. Quick Sort. First element is pivot
import random
test_list = []
for i in range(30):
    test_list.append(random.randint(0,100))

def sort(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    start = 1
    end = len(nums)-1
    swap = int
    while start <= end:
        try:
            while nums[start] < pivot:
                start += 1
                if start >= len(nums) or start > end:
                    raise Exception("End")
            while nums[end] > pivot:
                end -= 1
                if end == 0 or start > end:
                    raise Exception("End")
            swap = nums[end]
            nums[end] = nums[start]
            nums[start] = swap
            start += 1
            end -= 1
        except:
            pass
    nums[0] = nums[end]
    nums[end] = pivot
    nums[:end] = sort(nums[:end])
    nums[end+1:] = sort(nums[end+1:])
    return nums

#------------------------------------------------------------------------------------------------
#Lomuto Partition. Last elemenet is pivot
def sort2(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[-1]
    pIndex = 0
    i = 0
    while i < len(nums)-1:
        try:
            while nums[pIndex] <= pivot:
                pIndex += 1
                if pIndex == len(nums)-1:
                    raise Exception("end")
            i = pIndex
            while nums[i] > pivot:
                i += 1
                if i == len(nums):
                    raise Exception("end")
            if i != len(nums):
                swap = nums[i]
                nums[i] = nums[pIndex]
                nums[pIndex] = swap
        except:
            i = float('inf')
    nums[:pIndex] = sort2(nums[:pIndex])
    nums[pIndex+1:] = sort2(nums[pIndex+1:])
    return nums



print(test_list)
print(sort2(test_list))