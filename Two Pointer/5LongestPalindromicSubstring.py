class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_s = s[0]
        curr_s = ""

        
        for i in range(len(s)):
            # Odd cases
            h = i-1
            t = i+1
            while(h >= 0 and t <= len(s) - 1 and s[h] == s[t]):
                curr_s = s[h:t+1]
                if(len(max_s) < len(curr_s)):
                    max_s = curr_s
                h-=1
                t+=1
            
            # Even cases
            h = i
            t = i+1
            while(h >= 0 and t <= len(s) - 1 and s[h] == s[t]):
                curr_s = s[h:t+1]
                if(len(max_s) < len(curr_s)):
                    max_s = curr_s
                h-=1
                t+=1
            
        return max_s