class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for item in rows:
            for k in range(len(matrix[0])):
                matrix[item][k] = 0

        for item in cols:
            for k in range(len(matrix)):
                matrix[k][item] = 0
        
