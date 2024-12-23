class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        soln = [[0]*(i+1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(0,i+1,1):
                if j == 0 or j == i:
                    soln[i][j] = 1 
                else:
                    soln[i][j] = soln[i-1][j-1] + soln[i-1][j]
        
        return soln