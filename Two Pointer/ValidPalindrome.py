class Solution:
    def isPalindrome(self, s: str) -> bool:

        lower_s = s.lower()
        soln_s = ""

        # Process the string first
        for i in range(len(s)):
            if 97 <= ord(lower_s[i]) and ord(lower_s[i]) <= 122 or 48 <= ord(lower_s[i]) and ord(lower_s[i]) <= 57:
                soln_s += lower_s[i]

        # Use two pointer on the processed string
        h = 0
        t = len(soln_s) - 1
        while(h < t):            
            if(soln_s[h] != soln_s[t]):
                return False
            h+=1
            t-=1
        return True
