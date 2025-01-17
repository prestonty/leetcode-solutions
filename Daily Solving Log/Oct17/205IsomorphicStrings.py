class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sTot = {}
        tTos = {}
        word = ""
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in sTot and t[i] not in tTos:
                sTot[s[i]] = t[i]
                tTos[t[i]] = s[i]
            
            if t[i] in tTos and tTos[t[i]] == s[i] and s[i] in sTot and sTot[s[i]] == t[i]:
                word = word + sTot[s[i]]
        
        if word == t:
            return True
        return False
        
        
