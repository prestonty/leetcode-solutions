class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        i = len(stones) - 1
        while i > 1:
            if stones[i] == stones[i-1]:
                stones = stones[:i-1]
                i-=2 # iterate twice
            else:
                stones[i] -= stones[i-1]
                stones.pop(i-1)
                stones.sort()
                i-=1
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
            
            