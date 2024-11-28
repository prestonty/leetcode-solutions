class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = {}

        for item in arr:
            if item not in frequency:
                frequency[item] = 1
            else:
                frequency[item] +=1
        
        unique = set()
        for item in frequency:
            if frequency[item] not in unique:
                unique.add(frequency[item])
            else:
                return False
        
        return True