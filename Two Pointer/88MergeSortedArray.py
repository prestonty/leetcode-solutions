class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = 0
        p2 = 0
        
        # edge cases, empty array
        if n == 0:
            return
        
        if m == 0:
            nums1.clear()
            nums1 += nums2
            return

        # gotta do all this cause this questions input is a challenge in itself
        copy = nums1[:m]
        nums1.clear()
        for i in range(m):
            nums1.append(copy[i])

        # nums1 = nums1[:m]

        while p2 < n:
            if p1 == m + p2:
                nums1.append(nums2[p2])
                p2+=1
                p1+=1
            elif nums1[p1] > nums2[p2]:
                nums1.insert(p1, nums2[p2])
                p2+=1
                p1+=1
            elif nums2[p2] >= nums1[p1]:
                p1+=1