class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            smaller = s
            bigger = t
        elif len(s) > len(t):
            smaller = t
            bigger = s
        else:
            return s == t
        
        sp = 0
        tp = 0

        initialTp = 0

        while(sp < len(s)):
            tp = initialTp
            found = False
            while(tp < len(t) and sp < len(s)):
                if s[sp] == t[tp]:
                    initialTp = tp+1
                    sp+=1
                    found = True
                
                tp+=1
            if not found:
                return False
        
        return True