class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo stores the cost of each node, we can calculate right nodes using left most nodes
        memo = [-1]*(len(cost)+1) # include extra for the endpoint
        curr = len(cost) # start index of endpoint
        memo[curr] = min(self.findCostRecursively(cost, memo, curr-1), self.findCostRecursively(cost, memo, curr-2))

        return self.findCostRecursively(cost, memo, curr)
    
    def findCostRecursively(self, cost, memo, curr):
        if memo[curr] != -1:
            return memo[curr]
        
        if curr == 0 or curr == 1:
            memo[curr] = cost[curr]
        if curr > 1:
            memo[curr] = cost[curr] + min(self.findCostRecursively(cost, memo, curr-1), self.findCostRecursively(cost, memo, curr-2))
        
        return memo[curr]
