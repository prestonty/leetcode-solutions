class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        currAlt = 0
        for item in gain:
            currAlt+=item
            if currAlt > maxAlt:
                maxAlt = currAlt
        
        return maxAlt