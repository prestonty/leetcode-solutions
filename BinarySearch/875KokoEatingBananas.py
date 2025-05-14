class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest = 1
        biggest = max(piles)

        if h == len(piles):
            return biggest

        while smallest < biggest:
            k = (smallest+biggest) // 2
            time = 0 # time to eat bannanas at rate k
            for item in piles:
                time += math.ceil(item/k)
            
            if time > h:
                smallest = k+1
            else:
                biggest = k
            
        return smallest