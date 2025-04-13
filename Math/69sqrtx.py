class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 0):
            return 0
        elif(x == 1):
            return 1
            
        max_num = x
        min_num = 1
        current = x // 2

        while(min_num <= max_num):
            if(x // current > current):
                min_num = current + 1
            elif(x // current < current):
                max_num = current - 1
            else:
                return current
            current = (max_num+min_num) // 2

        return current

# Solution #2 (Worst solution)
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         current = 0
#         if(x == 0):
#             return 0

#         while(current*current <= x):
#             current+=1
#         return current - 1