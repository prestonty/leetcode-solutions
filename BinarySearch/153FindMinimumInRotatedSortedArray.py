class Solution:
    def findMin(self, nums: List[int]) -> int:
        h = 0
        t = len(nums) - 1

        # handle the case of array size 2
        if(len(nums) == 2):
            if nums[0] > nums[1]:
                return nums[1]
            return nums[0]
        # edge case, smallest is on the most left:
        if len(nums) > 2 and nums[len(nums) - 1] < nums[len(nums) - 2]:
            return nums[len(nums) - 1]


        mid = (h + t) // 2
        if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
            return nums[mid]

        while h != t:
            if nums[mid] < nums[t] and nums[mid] < nums[h] and h+1 == mid and t-1 == mid:
                break
            elif nums[mid] < nums[t]:
                t = mid
            elif nums[mid] > nums[h]:
                h = mid
            mid = (h + t) // 2

            if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                break
        
        return nums[mid]
        