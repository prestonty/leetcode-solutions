class Solution:
    def hIndex(self, citations: List[int]) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)

        for i in range(len(citations)):
            hashmap[citations[i]] = 0

        for i in range(len(citations)):
            hashmap[citations[i]]+=1

            for key in hashmap:
                if key != citations[i] and key < citations[i]:
                    hashmap[key]+=1
        
        h = 0
        for key in hashmap:
            if min(key, hashmap[key]) > h and hashmap[key] >= key:
                h = min(key, hashmap[key])
            elif min(key, hashmap[key]) > h:
                h = hashmap[key]
        
        return h



    # More optimized soln
    # class Solution:
    # def hIndex(self, citations: List[int]) -> int:
    #     from collections import defaultdict
    #     n = len(citations)
    #     bucket = [0]*(n+1)

    #     for c in citations:
    #         if c >= n:
    #             bucket[n] += 1  # holy smokes this ensures that c is not out of index!!!
    #         else:
    #             bucket[c] += 1 # never index out of bounds

    #     # concept of accumulation. We know that bucket[0] holds frequencies that are smaller than bucket[1].
    #     # so total # of items smaller than bucket[1] is bucket[0]+bucket[1]. Accumulation
    #     total = 0
    #     for i in range(n, 0, -1):
    #         total += bucket[i]
    #         if total >= i:
    #             return i
        
    #     return 0