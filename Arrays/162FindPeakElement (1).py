class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maximum = float('-inf')
        index = 0
        for i in range(len(nums)):
            if maximum < nums[i]:
                maximum = nums[i]
                index = i
                print("max: ", maximum)
                print("index: ", index)
        
        return index
            
        