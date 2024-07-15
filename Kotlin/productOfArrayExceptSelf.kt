class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        var output = IntArray(size = nums.size) {it -> 1}
        var temp = 1
        for (i in 0 until nums.size){
            output[i] *= temp
            temp *= nums[i]
        }
        temp = 1
        for (i in nums.size - 1 downTo 0){
            output[i] *= temp
            temp *= nums[i]
        }
        return output
    }
}