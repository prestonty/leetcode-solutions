class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        i = 0
        while i < len(nums):
            if nums[i] not in unique:
                unique.append(nums[i])
                i+=1
            else:
                nums.remove(nums[i])
        return len(nums)