class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        swapped = False

        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
                    swapped = True
            
            if not swapped:
                return
            