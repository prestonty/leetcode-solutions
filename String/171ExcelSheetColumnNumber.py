class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0

        for i in range(len(columnTitle)):
            num = (ord(columnTitle[i]) - 64) * (26 ** (len(columnTitle) - 1 - i))
            total += num
        
        return total