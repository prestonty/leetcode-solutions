class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique1 = set()
        unique2 = set()

	# wow this makes me really think of how I can optimize my soln (went from beating 5% to 95%)
        set1 = set(nums1) # first convert to set to remove duplicates
        set2 = set(nums2) # first convert to set to remove duplicates

        for item in set1:
            if item not in set2:
                unique1.add(item)
        
        for item in set2:
            if item not in set1:
                unique2.add(item)

        return [list(unique1), list(unique2)]