class Solution:
    def fib(self, n: int) -> int:
        memo = [-1]*(n+1) # for n = 0 case

        return self.fibHelper(n, memo)


    # helper
    def fibHelper(self, n, memo):
        
        if memo[n] != -1:
            return memo[n]
        
        if n == 0:
            memo[n] = 0
        elif n == 1:
            memo[n] = 1
        else:
            memo[n] = self.fibHelper(n-1, memo) + self.fibHelper(n-2, memo)

        return memo[n]