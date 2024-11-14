class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left = n

        # handle size one array
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            left -= 1

        for i in range(len(flowerbed)):
            if i == 0 and i < len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i+1] == 0 or i > 0 and i < len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 or i == len(flowerbed) - 1 and i - 1 >= 0 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                left -=1
        if(left <= 0):
            return True
        return False