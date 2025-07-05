class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # zeros stop you. As long as no zeros, its possible
        # TAKE PATHS that do not lead you to zero
        # Dynamic programming question
        # Brute force soln
        # have bool array that tracks possible paths. Iterate through nums and correct this bool path
        # if last index of bool path is true, return true, else return false

        # Problem - O(n^2)
        # We are re-checking too many. Already setting possiblePaths to true again

        # possiblePaths = [False] * len(nums)

        # possiblePaths[0] = True # Initialize the first path, we have access to it
        # maxDistance = 1
        # for i in range(len(nums)):
        #     if not possiblePaths[i]:
        #         if i > maxDistance:
        #             return False # Terminate early for false
        #         continue # Only go through second for loop if True (aka has access to this path)
            
        #     for j in range(maxDistance, min(len(nums), nums[i]+i+1)): # Absolute index, not relative steps
        #         possiblePaths[j] = True
        #         if j == len(nums) - 1:
        #             return True # Terminate early for true

        #     if nums[i] > maxDistance:
        #         maxDistance = nums[i]
            
        # return possiblePaths[len(nums) - 1]


        # Start from scratch. Keep track of furthest index, do not store in boolean array
        # If you reached farthest, then its possible to go to ANY point before farthest!! This is a fact!!

        # O(n) time complexity
        farthest = nums[0]
        for i in range(len(nums)):
            if i > farthest:
                return False  # you're stuck
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True   # you can reach the end

        # What I learned:
        # Use early terminating conditions (returning true or false IN the loop instead of after the loop)
        # We are NOT processing data, we are checking to see if a data structure meets the condition.
        # Notice how WE ARE NOT MODIFYING THE ORIGINAL!!! This is when we use early terminating condiitions

        # there are many possible paths, we need to find if there are none. Assume there is a path
        # Start at first index
        # First index unlocks future indices
        # Use [true, true, true, true, true]