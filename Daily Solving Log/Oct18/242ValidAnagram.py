class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 1
            elif s[i] in sMap:
                sMap[s[i]] += 1
            
            if t[i] not in tMap:
                tMap[t[i]] = 1
            elif t[i] in tMap:
                tMap[t[i]] += 1
        
        for ch in s:
            # Need to check if character in s is in t
            if ch not in tMap or sMap[ch] != tMap[ch]:
                return False
        
        return True