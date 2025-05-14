class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # Edge cases (index 0 and len-1)
        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
        elif nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]
        
        # Algorithm
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            
            if middle%2 == 0 and nums[middle] == nums[middle+1] or middle%2 == 1 and nums[middle-1] == nums[middle]:
                left = middle+1
            else:
                right = middle
        return nums[left]