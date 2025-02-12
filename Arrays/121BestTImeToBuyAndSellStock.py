class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest = float('inf')

        for price in prices:
            if price < lowest:
                lowest = price
            
            if price - lowest > maxP:
                maxP = price - lowest
        
        return maxP