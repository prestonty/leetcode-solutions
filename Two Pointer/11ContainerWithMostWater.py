class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        h = 0
        t = len(heights) - 1

        while(h < t):
            if heights[h] > heights[t]:
                localMin = heights[t]
            else:
                localMin = heights[h]
            v = (t-h) * localMin
            if v > maxVol:
                maxVol = v
            
            if heights[h] > heights[t]:
                t-=1
            else:
                h+=1

        return maxVol