class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        set1 = set(list(word1))
        set2 = set(list(word2))

        if(len(word1) != len(word2) or set1 != set2):
            return False
        hashmap1 = {}
        hashmap2 = {}

        # using zip() and combining it into 1 for loop is faster than 2 separate for loops (perfect when arrays are same size)
        for char1, char2 in zip(word1, word2):
            if(char1 not in hashmap1):
                hashmap1[char1] = 1
            else:
                hashmap1[char1]+=1
            if(char2 not in hashmap2):
                hashmap2[char2] = 1
            else:
                hashmap2[char2]+=1

        group1 = list(hashmap1.values())
        group2 = list(hashmap2.values())

        group1.sort()
        group2.sort()
        if(len(group1) != len(group2)):
            return False
        for i in range(len(group1)):
            if group1[i] != group2[i]:
                return False

        return True