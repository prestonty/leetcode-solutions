# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        m = l + math.floor((r - l)/2)

        while(l < r):
            if isBadVersion(m) == True:
                r = m
            else:
                l = m+1

            m = l + math.floor((r - l)/2)
        
        return m