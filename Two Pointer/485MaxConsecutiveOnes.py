class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0

        for num in nums:
            if num == 0:
                count = 0
                continue
            else:
                count += 1

            if count > maxCount:
                maxCount = count

        return maxCount