class Solution:
    def isHappy(self, n: int) -> bool:
        squareSums = set()
        currentSum = 0
        
        # do while loop scuffed
        stringNum = str(n)
        for i in range(len(stringNum)):
            currentSum = currentSum + int(stringNum[i])**2
        
        # Early terminating condition
        if currentSum == 1:
            return True
        
        while(currentSum not in squareSums):
            squareSums.add(currentSum)
            
            stringNum = str(currentSum)
            currentSum = 0
            for i in range(len(stringNum)):
                currentSum = currentSum + int(stringNum[i])**2
        
            if currentSum == 1:
                return True
        
        # Breaking out of loop means there is a duplicate, aka infinite loop
        return False
            