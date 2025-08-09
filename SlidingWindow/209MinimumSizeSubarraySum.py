class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            # only 10 lines of code!!!!!
            # sliding window. calculate the sum between the item
            # keep track of variable in total. So calculating the total is O(1)
            total = 0
            l,r = 0,0
            small_l = 0
            small_r = len(nums)
            rChanged = True
            found = False
            while r < len(nums):
                if nums[r] > target:
                    return 1 # one item subarray
                if rChanged:
                    total+=nums[r] # adding this each time! even when r doesnt change

                if total < target:
                    r+=1
                    rChanged = True
                else:
                    if small_r - small_l + 1 > r - l + 1:
                        small_r = r
                        small_l = l

                    total-=nums[l]
                    l+=1
                    rChanged = False

                    if total >= target and small_r - small_l + 1 > r - l + 1:
                        small_r = r
                        small_l = l
                        found = True
            
            if not found:
                return 0
            return small_r - small_l + 1