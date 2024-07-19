class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = float('inf')
        total_profit = 0
        for price in prices:
            if price < bp:
                bp = price
            else:
                total_profit += price - bp
                bp = price
        return total_profit