# First leetcode hard, I got help for this soln
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # greedy algorithm
        numOperations = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                numOperations += target[i] - target[i-1]
        
        return numOperations


# class Solution:
#     def minNumberOperations(self, target: List[int]) -> int:
#         return self.helper(target, 0, len(target))
        
#     def helper(self, target: List[int], start, end) -> int:
# 	#Soln sucks cause min() function is O(n) each time and O(n^2) worst case
#         minimum = min(target[start:end])

#         if minimum == 0:
#             return 0

#         # when target length is 1
#         if end - start == 1:
#             return minimum

#         # when target length is not 1
#         numOperations = 0
#         h = start
#         t = start
#         foundZero = True # assume zero is found already to initial case
#         while(t < end):
#             target[t] -= minimum
#             if(target[t] == 0 and foundZero == True):
#                 # back to back zeros
#                 t+=1
#                 h = t
#             elif target[t] == 0:
#                 # first time finding zero
#                 numOperations += self.helper(target, h, t)
#                 t+=1
#                 h = t
#                 foundZero = True
#             elif target[t] != 0:
#                 foundZero = False
#                 t+=1
#         # catch final case when last element of target is not zero
#         if foundZero == False:
#             numOperations += self.helper(target, h, t)
#         return minimum + numOperations