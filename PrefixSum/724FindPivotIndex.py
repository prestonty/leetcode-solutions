class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        maxSum = 0
        for item in nums:
            maxSum += item

        # check first index
        if maxSum - nums[0] == 0:
            return 0

        
        currSum = 0
        for i in range(0, len(nums)-1):
            currSum += nums[i]
            print("currSum: ", currSum)
            print("maxSum-nums[i]: ", maxSum-nums[i+1])
            if(currSum * 2 == maxSum-nums[i+1]):
                return i+1
        
        # check last index at the very end cause there might be a solution before it
        if maxSum - nums[len(nums) - 1] == 0:
            return len(nums) - 1

        return -1