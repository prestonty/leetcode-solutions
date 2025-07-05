class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Notes: ----------------------------------------
        # O(n)
        # touch every element once. Circular array.
        # Always rotates to the right
        # If index + k > len - 1, (index + k) % (len-1)
        # Modify existing array
        # Copy into new array, and then copy back into existing array
        # Notes end ----------------------------------------

        # 1. brute force soln (solve in new array, copy back)
        if len(nums) == k:
            return
        soln = [0] * len(nums)
        for i in range(len(nums)):
            soln[i] = nums[(len(nums) - k + i) % (len(nums))]
        for i in range(len(soln)):
            nums[i] = soln[i]