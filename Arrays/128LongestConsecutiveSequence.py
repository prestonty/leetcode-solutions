class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        soln = []
        maxCount = 0
        for num in hashset:
            if num - 1 not in hashset:
                count = 0
                currNum = num
                while currNum in hashset:
                    count+=1
                    currNum+=1

                    if count > maxCount:
                        maxCount = count
        
        return maxCount