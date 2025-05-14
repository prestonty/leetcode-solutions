class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return min(nums)

        l, r = 0, len(nums) - 1
        m = (l + r)//2
        while l < r:
            
            if nums[m] > nums[l] and nums[m] > nums[r]:
                l = m
            elif nums[m] < nums[l] and nums[m] < nums[r]:
                r = m
            elif nums[l] < nums[m] and nums[m] < nums[r]:
                r = m
            else:
                break
            m = (l + r)//2
        
        if nums[r] > nums[l]:
            return nums[l]
        return nums[r]