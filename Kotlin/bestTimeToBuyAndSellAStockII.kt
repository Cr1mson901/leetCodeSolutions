class Solution {
    fun maxProfit(prices: IntArray): Int {
        var low = prices[0]
        var total = 0
        for (price in prices){
            if(price < low){
                low = price
            }else{
                total += (price - low)
                low = price
            }
        }
        return total
    }
}