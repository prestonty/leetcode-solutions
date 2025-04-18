class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainList = {}
        soln = []
        count = 0
        for item in strs:
            # Create list of items based on length
            sortedItem = ''.join(sorted(item))
            if sortedItem not in mainList:
                mainList[sortedItem] = count # count is the index of item in list
                soln.append([item])
                count+=1
            else:
                soln[mainList[sortedItem]].append(item)
        
        return soln
