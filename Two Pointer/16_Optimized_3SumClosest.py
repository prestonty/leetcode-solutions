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

                # So diff determines the closest sum
                if(diff == 0):
                    return curr_sum
                elif(diff < smallestDiff):
                    smallestDiff = diff
                    soln = curr_sum

                # The closest sum determines how pointers change
                if(curr_sum > target):
                    # we can get a smaller diff if we decrease curr_sum
                    t-=1
                else:
                    # by increasing h, we increase curr_sum, making it closer to target for a smaller diff
                    h+=1

        return soln