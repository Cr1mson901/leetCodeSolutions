class Solution {
    fun maxProfit(prices: IntArray): Int {
        var bp = prices[0]
        var maxProfit = 0
        for (price in prices){
            if (price < bp){
                bp = price
            }else if(price - bp > maxProfit){
                maxProfit = price - bp
            }
        }
        return (maxProfit)
    }
}