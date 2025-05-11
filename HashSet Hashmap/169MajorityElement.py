class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = {}
        maximum_count = 0
        maximum = nums[0]

        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                table[num]+=1
            if table[num] > maximum_count:
                maximum = num
                maximum_count = table[num]
        
        return maximum