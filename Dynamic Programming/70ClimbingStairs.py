class Solution:
    def climbStairsHelper(self, n, memo):
        if memo[n] != -1:
            return memo[n]

        # if it dont pass the vibe check
        if n == 0 or n == 1:
            memo[n] = 1
            return 1

        if n >= 2:
            memo[n] = self.climbStairsHelper(n-2, memo) + self.climbStairsHelper(n-1, memo)
            return memo[n]

    # This was the original function
    def climbStairs(self, n: int) -> int:
        # This is the data structure to store results in this pattern. We are using memoization
        memo = [-1] * (n + 1) # default value is -1 to show it DNE. Must be n+1 to account for when n = 0

        # any time you reference something inside the class, you must use self
        # call the function to initiate the recursive process
        return self.climbStairsHelper(n, memo)

    # define a function that does the recursive process