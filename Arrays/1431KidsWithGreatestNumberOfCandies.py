class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = 0
        soln = [False]*len(candies)

        for item in candies:
            if item > maximum:
                maximum = item
        
        for i in range(len(candies)):
            if candies[i] >= maximum - extraCandies:
                soln[i] = True
        
        return soln