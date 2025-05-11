class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        soln = []

        for i in range(len(sorted_nums)):
            if(sorted_nums[i] > 0):
                break

            # skip duplicate i
            if(i > 0 and sorted_nums[i] == sorted_nums[i-1]):
                continue
                
            h = i+1
            t = len(sorted_nums) - 1
            while(h < t):
                total = sorted_nums[h] + sorted_nums[t] + sorted_nums[i]
                if(total == 0):
                    soln.append([sorted_nums[i], sorted_nums[h], sorted_nums[t]]) # you cannot use "not in soln" to check for duplicates since that is O(n^3) instead of O(n^2). Be careful of built in functions, you need to know your time complexities. Its better if you do everything yourself.
                    # duplicates arise from encountering the same sorted_nums[i] back to back or for h and t. So we need these while loops to make sure they are unique relative to the previous one, not relating t to h.
                
                    while h < t and sorted_nums[h] == sorted_nums[h + 1]:
                        h += 1
                    while h < t and sorted_nums[t] == sorted_nums[t - 1]:
                        t -= 1
                    h+=1
                    t-=1
                elif(total > 0):
                    t-=1
                elif(total < 0):
                    h+=1
        
        return soln