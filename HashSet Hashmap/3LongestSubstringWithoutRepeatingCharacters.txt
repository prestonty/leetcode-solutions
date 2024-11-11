class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        maxLen = 0
        currLen = 0
        head = 0
        tail = 0

        for i in range(len(s)):
            if s[i] in characters:
                while s[head] != s[i]:
                    characters.remove(s[head])
                    head+=1 # make sure head becomes one after s[i] 
                head+=1
                currLen = tail - head + 1
                if maxLen < currLen:
                    maxLen = currLen
            else:
                currLen = tail - head + 1
                characters.add(s[i])
                if maxLen < currLen:
                    maxLen = currLen
            tail+=1
        
        return maxLen