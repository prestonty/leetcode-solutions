class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        increase = True
        for i in range(len(nums) - 1):
            if increase and nums[i] > nums[i + 1]:
                return i
            elif nums[i] < nums[i + 1]:
                increase = True
            elif nums[i] > nums[i + 1]:
                increase = False
        
        # check end case:
        return len(nums) - 1
            
        