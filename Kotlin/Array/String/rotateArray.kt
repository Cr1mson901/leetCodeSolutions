class Solution {
    fun rotate(nums: IntArray, k: Int): Unit {
        if (nums.size == 1 || k == 0){
            return
        }
        var pivot = k
        while (pivot >= nums.size){
            pivot = pivot - nums.size
        }
        if (pivot == 0) {return}
        pivot = nums.size - pivot
        var tempArray = nums.slice(0..pivot-1)
        for (i in (0..nums.size-pivot-1)){
            nums[i] = nums[pivot+i]
        }
        for (i in (0..tempArray.size-1)){
            nums[i + nums.size - pivot] = tempArray[i]
        }
    }
}