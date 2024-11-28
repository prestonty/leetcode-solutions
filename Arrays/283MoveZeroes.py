class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        countZeros = 0
        curr = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr] = nums[i]
                curr+=1
            else:
                countZeros+=1

        for i in range(countZeros):
            nums[curr] = 0
            curr+=1
        
