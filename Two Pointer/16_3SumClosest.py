class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        soln = nums[0] + nums[1] + nums[2] # default case
        smallestDiff = abs(soln - target)
        
        for i in range(len(nums) - 2):
            if nums[i] > 0 and nums[i] > target: # If positive and nums[i] is greater than target, you cant get any closer
                break

            h = i+1
            t = len(nums) - 1

            while(h < t):
                curr_sum = nums[i] + nums[h] + nums[t]
                diff = abs(target - curr_sum)

                if(h+1 < len(nums) and abs(nums[i] + nums[h+1] + nums[t] - target) < diff):
                    while(nums[h] == nums[h+1]): # Make sure it is unique (skip duplicates)
                        h+=1
                    h+=1
                elif(t-1 >= 0 and abs(nums[i] + nums[h] + nums[t-1] - target) < diff):
                    while(nums[t] == nums[t-1]): # Make sure it is unique (skip duplicates)
                        t-=1
                    t-=1
                elif(target >= 0):
                    h+=1 # If we want to become closer to target, we increase by moving h to right
                else:
                    t-=1 # To decrease our sum and move towards negative, we decrease t by moving t to left
                
                if(diff == 0):
                    return target
                elif(diff < smallestDiff):
                    smallestDiff = diff
                    soln = curr_sum

        return soln