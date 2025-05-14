class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix) - 1
        vm = math.floor((top + bottom)/2) # vertical middle
        
        while top < bottom:
            if target > matrix[vm][len(matrix[0]) - 1]:
                top = vm + 1
            elif target < matrix[vm][0]:
                bottom = vm - 1
            else:
                break
            vm = math.floor((top + bottom)/2)

        left, right = 0, len(matrix[0]) - 1
        hm = math.floor((left+right)/2) # horizontal middle
        while left < right:
            if target > matrix[vm][hm]:
                left = hm + 1
            elif target < matrix[vm][hm]:
                right = hm - 1
            else:
                break
            hm = math.floor((left+right)/2)
        
        if matrix[vm][hm] == target:
            return True
        return False

