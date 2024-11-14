class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]

        count = 1
        i = 0
        iMax = n
        j = 0
        jMax = n
        maximum = n

        iterations = n

        while count <= n**2:
            for k in range(iterations):
                matrix[i][j] = count
                count+=1
                j+=1
            j-=1
            i+=1
            iterations-=1
            if count > n**2:
                break
            for k in range(iterations):
                matrix[i][j] = count
                count+=1
                i+=1
            i-=1
            j-=1
            
            if count > n**2:
                break
            for k in range(iterations):
                matrix[i][j] = count
                count+=1
                j-=1
            j+=1
            i-=1
            iterations-=1

            if count > n**2:
                break
            for k in range(iterations):
                matrix[i][j] = count
                count+=1
                i-=1
            i+=1
            j+=1

        return matrix