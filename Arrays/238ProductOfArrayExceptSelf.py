class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        gcm = 1
        hasZero = False
        multipleZeros = False
        allZeros = True
        soln = [0]*len(nums)

        for num in nums:
            if hasZero and num == 0:
                multipleZeros = True
            elif num == 0:
                hasZero = True
            else:
                gcm *= num
                allZeros = False

        if allZeros: # early termination
            return soln

        for i in range(len(nums)):
            if(hasZero == True and nums[i] == 0 and not multipleZeros):
                soln[i] = gcm
            elif not hasZero:
                soln[i] = int(gcm / nums[i])

        return soln