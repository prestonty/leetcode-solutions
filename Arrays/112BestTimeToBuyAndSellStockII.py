class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        start = prices[0]
        for i in range(len(prices)):
            if prices[i] > start:
                total += prices[i] - start
            start = prices[i]

        return total