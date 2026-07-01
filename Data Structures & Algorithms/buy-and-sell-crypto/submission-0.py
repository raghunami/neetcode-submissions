class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0

        for price in prices:
            minimum = min(minimum, price)
            max_profit = max(max_profit, price - minimum)

        return max_profit
            

        