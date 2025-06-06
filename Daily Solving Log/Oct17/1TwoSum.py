class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if((target - nums[i]) not in hashmap):
                hashmap[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in hashmap and i != hashmap[nums[i]]:
                return [i, hashmap[nums[i]]]