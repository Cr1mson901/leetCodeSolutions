class Solution {
    fun canJump(nums: IntArray): Boolean {
        if(nums.size < 2){return true}
        var energy = nums[0]
        for (i in (0..nums.size - 2)){
            if (nums[i] > energy){
                energy = nums[i]
            }
            if (energy == 0){
                return false
            }
            energy--
        }
        return true
    }
}