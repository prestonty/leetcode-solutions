class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        candidates = set()
        blackList = set()
        for num in nums:
            if num not in candidates and num not in blackList:
                candidates.add(num)
            elif num in candidates and num in blackList:
                candidates.remove(num)
            elif num in candidates and num not in blackList:
                candidates.remove(num)
                blackList.add(num)
        for num in candidates:
            return num