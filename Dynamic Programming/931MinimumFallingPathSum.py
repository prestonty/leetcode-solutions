class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = [[-101]*len(matrix[0]) for _ in range(len(matrix))]
        minimum = float('inf')
        for m in range(len(matrix[0])):
            current = self.falling(matrix, memo, 0, m)
            if current < minimum:
                minimum = current
        return minimum
        
    def falling(self, matrix, memo, n, m):
        if(memo[n][m] != -101):
            return memo[n][m]

        if n == len(matrix)-1:
            memo[n][m] = matrix[n][m] # its returning the last element, so no need for minimum since its only 1 element
        elif n < len(matrix) - 1 and len(matrix[0]) == 1:
            memo[n][m] = matrix[n][m] + self.falling(matrix, memo, n+1, m)
        elif n < len(matrix) - 1  and m == 0:
            memo[n][m] = matrix[n][m] + min(self.falling(matrix, memo, n+1, m), self.falling(matrix, memo, n+1, m+1))
        elif n < len(matrix) - 1 and m == len(matrix[0]) - 1:
            memo[n][m] = matrix[n][m] + min(self.falling(matrix, memo, n+1, m), self.falling(matrix, memo, n+1, m-1))
        elif n < len(matrix) - 1 and m > 0 and m < len(matrix[0]) - 1:
            memo[n][m] = matrix[n][m] + min(self.falling(matrix, memo, n+1, m), self.falling(matrix, memo, n+1, m+1), self.falling(matrix, memo, n+1, m-1))

        return memo[n][m]
