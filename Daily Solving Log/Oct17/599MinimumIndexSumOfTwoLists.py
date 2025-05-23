class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lowestSum = float('inf') # debugging this genuinely pissed me off
        commonStrings = []
        map2 = {}
        
        
        for i in range(len(list2)):
            map2[list2[i]] = i # store index as value
        
        for i in range(len(list1)):
            if list1[i] in map2 and i + map2[list1[i]] < lowestSum:
                commonStrings.clear() # empty it out if found lower sum
                lowestSum = i + map2[list1[i]]
                commonStrings.append(list1[i])
            elif list1[i] in map2 and i + map2[list1[i]] == lowestSum:
                commonStrings.append(list1[i])


        return commonStrings
                