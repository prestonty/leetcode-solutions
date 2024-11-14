class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1]*(n+1)

        return self.tribonacciRecursive(n, memo)
    
    def tribonacciRecursive(self, n, memo):
        if memo[n] != -1:
            return memo[n]
        
        if n == 0:
            memo[n] = 0
        elif n == 1 or n == 2:
            memo[n] = 1
        else:
            memo[n] = self.tribonacciRecursive(n-1, memo) + self.tribonacciRecursive(n-2, memo) + self.tribonacciRecursive(n-3, memo) 
        
        return memo[n]
        