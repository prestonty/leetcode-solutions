class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Edge cases, len 2
        if len(nums) == 2 and target == nums[1]:
            return 1

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2

            if target == nums[m]:
                return m
            elif nums[m] > nums[r] and (target > nums[m] or target < nums[l]): # break on right, smallest on right
                l = m+1
            elif nums[m] > nums[r] and (target <= nums[m] and nums[l] <= target): # break on right, smallest on left
                r = m
            elif nums[m] < nums[r] and (target > nums[r] or target <= nums[m]): # break is on left, smallest on right
                r = m
            elif nums[m] < nums[r] and (target < nums[r] and target < nums[m]): # break is on left, smallest on left
                l = m+1
            elif nums[l] <= nums[m] < nums[r] and target < nums[m]: # When its a regular array
                r = m
            else:
                l = m+1
        
        if nums[l] == target:
            return l
        return -1