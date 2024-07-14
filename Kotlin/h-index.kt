class Solution {
    fun hIndex(citations: IntArray): Int {
        citations.sortDescending()
        var h = 0
        for(i in 0 until citations.size){
            if (h < citations[h]){
                h++
            }
        }
        return h
    }
}