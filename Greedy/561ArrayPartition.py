class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        minSum = 0
        for i in range(0, len(nums) - 1, 2):
            minimum = min(nums[i], nums[i+1])
            minSum +=minimum
        
        return minSum