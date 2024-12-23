class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num]+=1

        soln = []
        for i in range(k):
            highestIndex = 0
            numberOfHighestIndex = -1 # should never occur
            for key in hashmap: # for each loop always uses key
                if hashmap[key] > highestIndex:
                    highestIndex = hashmap[key] # set to key which is number
                    numberOfHighestIndex = key
            soln.append(numberOfHighestIndex)
            # To avoid adding same number again, we must remove from hashmap
            hashmap.pop(numberOfHighestIndex)
        
        return soln