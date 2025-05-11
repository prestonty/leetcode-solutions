class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = 0
        t = len(numbers) - 1

        while(numbers[h] + numbers[t] != target):
            total = numbers[h] + numbers[t]
            if(total > target):
                t-=1
            elif(total < target):
                h+=1
        
        return [h+1,t+1]