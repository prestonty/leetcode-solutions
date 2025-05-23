class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = [1, i]
            else:
                hashmap[s[i]] = [2, -1] # set to values indicating duplicate
        
        
        smallestIndex = float('inf')

        # This works because we are iterating through the word from left to right meaning index is already from 0 to len(s)
        for ch in s:
            if hashmap[ch][0] == 1 and hashmap[ch][1] != -1:
                return hashmap[ch][1]
        
        return -1
        
