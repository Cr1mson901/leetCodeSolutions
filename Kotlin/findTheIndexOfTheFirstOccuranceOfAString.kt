class Solution {
    fun strStr(haystack: String, needle: String): Int {
        var answer = 0
        var counter = 0
        var i = 0
        while (i < haystack.length){
            if (haystack[i] == needle[counter]){
                counter++
                if (counter == needle.length){
                    return answer
                }
                i++
            }
            else{
                counter = 0
                i = answer + 1
                answer = i
            }
        }
        return -1
    }
}