class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split()
        soln = ""
        for i in range(len(arr)):
            soln = arr[i] + " " + soln

        soln = soln.strip()
        return soln