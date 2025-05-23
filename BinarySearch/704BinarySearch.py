class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1

        middle = int((head + tail) // 2)

        if nums[middle] == target:
            return middle

        while target != nums[middle]:
            if head != tail and target > nums[middle] and middle <= len(nums) - 1:
                head = middle + 1
            elif head != tail and target < nums[middle] and middle >= 0:
                tail = middle - 1
            else:
                return -1

            middle = int((tail + head) // 2)

        return middle