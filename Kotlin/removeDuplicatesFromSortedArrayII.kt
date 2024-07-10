class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var counter = 0
        for (i in nums.size - 1 downTo 2){
            if (nums[i] == nums[i-2]){
                counter++
                if (nums.size - 1 != i){
                    for (j in i..(nums.size - counter - 1)){
                        nums[j] = nums[j+1]
                    }
                }
            }
        }
        return nums.size - counter
    }
}