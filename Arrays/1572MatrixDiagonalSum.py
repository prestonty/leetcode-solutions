class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0

        for i in range(len(mat)):
            total += mat[i][i]
            # only works for odd
            if len(mat) % 2 == 1 and not (i == int(math.floor(len(mat) / 2))):
                total += mat[i][len(mat) - 1 - i]
            elif len(mat) % 2 == 0:
                total += mat[i][len(mat) - 1 - i]
            
        return total