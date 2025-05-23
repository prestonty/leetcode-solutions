class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        h = 0
        t = 0
        spare = k
        maximum = 0
        currLen = 0

        if k == 0:
            startCombo = False
            # completely different algorithm
            for i in range(len(nums)):
                if nums[i] == 1 and not startCombo:
                    h = i # how do i set as first
                    t = i # restart combo
                    startCombo = True
                elif nums[i] == 1:
                    t = i
                elif nums[i] == 0:
                    startCombo = False
                
                if nums[t] != 0 or nums[h] != 0:
                    maximum = t - h + 1
        else:
            for i in range(len(nums)):
                if nums[i] == 0 and spare > 0:
                    print("Case 1")
                    spare -= 1
                elif nums[i] == 0 and spare <= 0:
                    print("Case 2")
                    if nums[h] == 0:
                        # if head already on a 0 (using a spare)
                        if nums[h] == 0:
                            h+=1
                        # make sure its at a zero
                    else:
                        while nums[h] != 0:
                            h+=1
                        h+=1

                currLen = t - h + 1
                t+=1

                # currLen = t - h
                if currLen > maximum:
                    maximum = currLen
        
        return maximum