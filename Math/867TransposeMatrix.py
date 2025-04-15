class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        soln = [[0]*(len(matrix)) for i in range(len(matrix[0]))]
        
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                 soln[i][j] = matrix[j][i]
        
        return soln