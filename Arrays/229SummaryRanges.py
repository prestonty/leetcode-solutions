class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        prev = 0
        currentIndex = 0
        soln = []
        for i in range(len(nums)):

            if i == 0:
                soln.append(str(nums[i]))
            elif prev+1 != nums[i] and i < len(nums) - 1:
                # its not consecutive
                if(soln[currentIndex] != str(prev)):
                    soln[currentIndex] = soln[currentIndex] + "->" + str(prev)

                if(i < len(nums) - 1):
                    soln.append(str(nums[i]))
                currentIndex+=1
            elif i == len(nums) - 1:
                if(prev+1 == nums[i]):
                    soln[currentIndex] = soln[currentIndex] + "->" + str(nums[i])                    
                else:
                    if(soln[currentIndex] != str(prev)):
                        soln[currentIndex] = soln[currentIndex] + "->" + str(prev)
                    soln.append(str(nums[i]))
            
            prev = nums[i]

        return soln