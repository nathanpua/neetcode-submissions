class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxprice = float('-inf')

        # Iterate from right to left
        for i in range(len(prices) - 1, -1, -1):
            # update the maxprice if we see a higher price
            maxprice = max(maxprice, prices[i])

            # calculate profit = maxprice seen so far - cur price
            profit = max(profit, maxprice - prices[i])

        return profit