class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            profit = max(prices[i] - buy, profit)
            buy = min(buy, prices[i])

        return profit