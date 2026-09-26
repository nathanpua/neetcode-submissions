class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        maxprice = prices[-1]
        
        for i in range(len(prices) - 1, -1, -1):
            maxprice = max(maxprice, prices[i])
            profit = max(profit, maxprice - prices[i])

        return profit