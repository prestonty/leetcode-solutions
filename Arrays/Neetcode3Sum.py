class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Soln does not work on leetcode, time limit exceeded
        soln = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if(nums[i] + nums[j] + nums[k] == 0):
                        potential = sorted([nums[i], nums[j], nums[k]])
                        if(potential not in soln):
                            soln.append(potential)
        
        return soln
        