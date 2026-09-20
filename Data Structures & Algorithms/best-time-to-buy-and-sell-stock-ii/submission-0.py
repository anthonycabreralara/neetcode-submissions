class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for p in prices:
            if p - buy > 0:
                profit += p - buy
                buy = p
            else:
                buy = min(buy, p)
        
        return profit