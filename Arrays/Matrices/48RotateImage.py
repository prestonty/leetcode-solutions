class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        Square matrices only

        0,0 -> 2,0
        2,0 -> 0,2
        0,2 -> 2,2
        2,2 -> 0,0

        All relative to the origin.

        Two cases - when there is a centre in the matrix (odd) and even matrix (no centre)

        1. Odd -> 
        """

        a = len(matrix) // 2
        b = math.ceil(len(matrix) / 2)

        n = len(matrix)
        for j in range(a): # short
            for k in range(b): # long
                # replace top right with top left                
                    temp = matrix[k][b + j]
                    matrix[k][b + j] = matrix[a-1-j][k]

                    # Replace bottom right with top right
                    temp2 = matrix[b+j][n-1-k]
                    matrix[b+j][n-1-k] = temp

                    # Replace bottom left with bottom right
                    temp = matrix[n-1-k][a-1-j]
                    matrix[n-1-k][a-1-j] = temp2

                    # Replace top left with bottom left
                    matrix[a-1-j][k] = temp
                