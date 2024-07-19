class Solution {
    fun removeElement(nums: IntArray, gold: Int): Int {
        var counter = 0
        val size = nums.size - 1
        for (i in (size downTo 0)){
            if (nums[i] == gold){
                if (size - i != counter){
                    nums[i] = nums[size - counter]
                    nums[size - counter] = gold
                }
                counter++
            }
        }
        return size - counter + 1
    }
}