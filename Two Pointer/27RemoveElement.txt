class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        if len(nums) == 0:
            return count
        
        head = 0 # keeps track of front
        tail = len(nums) - 1 # will be used to move elements equal to val to back

        # tail must point to element not equal to val
        while nums[tail] == val and tail >= 0:
            tail-=1

        # case where nums only contains val
        if tail == -1:
            return count

        # iterate through list: either swap to back when encounter val or keep traversing (increase count either way)
        for i in range(len(nums)):
            if nums[head] == val:
                temp = nums[tail]
                nums[tail] = nums[head]
                nums[head] = temp
                tail -= 1 # tail move down since it points to val
            
            # make sure tail points to element not equal to val
            while nums[tail] == val and tail >= 0:
                tail-=1

            count+=1
            head+=1 # traverse through list using head

            # scuffed conditions to break loop
            if head > tail or tail < 0 or head > len(nums) - 1 or head == tail and nums[head] == val:
                return count
        
        return count