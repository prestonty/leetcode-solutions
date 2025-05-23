class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                nums[k] = nums[i]
                k+=1
            elif hashmap[nums[i]] < 2:
                hashmap[nums[i]]+=1 # change it to opened
                nums[k] = nums[i]
                k+=1

        return k