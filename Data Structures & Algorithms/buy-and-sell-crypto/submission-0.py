class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window = 0
        index = 0
        max_profit = 0
        for price in prices:
            while window < len(prices):
                print("" + str(prices[window]) + " - " + str(price) + " = " + str(prices[window] - price))
                max_profit = max(max_profit, prices[window] - price)
                window += 1
            index += 1
            window = index + 1
        return max_profit
