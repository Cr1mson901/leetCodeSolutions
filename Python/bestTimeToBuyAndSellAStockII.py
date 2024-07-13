class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = float('inf')
        max_profit = 0
        for price in prices:
            if price < bp:
                bp = price
            elif price - bp > max_profit:
                max_profit = price - bp
        return max_profit