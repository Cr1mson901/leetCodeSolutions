class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        var i = n - 1
        var j = m - 1
        var k = n + m - 1
        while (i >= 0){
            if (j < 0){
                for (l in (i downTo 0)){
                    nums1[l] = nums2[l]
                }
                break
            }
            if (nums2[i] >= nums1[j]){
                nums1[k] = nums2[i]
                i--
                k--
            }else{
                nums1[k] = nums1[j]
                j--
                k--
            }
        }
    }
}