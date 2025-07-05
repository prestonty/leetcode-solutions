class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0

        soln = [0]*(len(matrix[0])*len(matrix))
        count = 0
        minX, maxX = -1, len(matrix[0])
        minY, maxY = -1, len(matrix)

        options = [(1,0), (0,1), (-1,0), (0,-1)]
        direction = 0
        while count < len(soln):
            soln[count] = matrix[j][i]
            count+=1
            di, dj = options[direction]
            
            # Peak into the future before proceeding with i,j
            future_x = i+di
            future_y = j+dj
            if not (minX < future_x and future_x < maxX and minY < future_y and future_y < maxY):
                # Change direction when bound is hit. Then add using new direction
                
                # Given the existing direction, we will determine the new bounds
                if direction == 0:
                    minY+=1
                elif direction == 1:
                    maxX-=1
                elif direction == 2:
                    maxY-=1
                elif direction == 3:
                    minX+=1

                # After determining new bounds, change the direction
                direction = (direction+1)%4

                i += options[direction][0]
                j += options[direction][1]
            else:
                # If bound is not hit, then continue with the increase and set i to its future_x
                i = future_x
                j = future_y
        return soln


                