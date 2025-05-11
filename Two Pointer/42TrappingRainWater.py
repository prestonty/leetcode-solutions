class Solution:
    def trap(self, height: List[int]) -> int:
        if(len(height) < 3):
            return 0

        maxNum = max(height)
        numMax = height.count(maxNum)
        currMax = 0
        # Check if first index at l is a maxNum:
        if height[0] == maxNum:
            currMax+=1
        # Iterate from left to right when the maximum height is Not at the beginning of the array and there is more than 1 max height
        l, r = 0, 1
        vol = 0
        if not (numMax == 1 and height[0] == maxNum):
            vol = (len(height) - 2)*height[l]
            while(r <= len(height) - 1):
                if height[r] < height[l]:
                    if r == len(height) - 1:
                        vol -= (height[l] - height[r])*(r-l-1)
                        l = r
                    else:
                        vol -= height[r]
                elif height[r] > height[l]:
                    if height[r] == maxNum:
                        currMax+=1

                    if currMax == numMax:
                        vol -= (len(height) - r - 1)*height[l]
                        l = r
                        break
                    else:
                        vol += ((len(height) - 2 - r)*height[r]) # with area with max

                        vol -= (len(height) - r - 1)*height[l]
                    l = r
                else:
                    # when heights are equal
                    if height[r] == maxNum:
                        currMax+=1
                    
                    if currMax == numMax:
                        vol -= (len(height) - r - 1)*height[l]
                        l = r
                        break
                    elif r != len(height) - 1:
                        vol -= height[r]
                    
                    l = r
                r+=1
        
        # Now that l is at the index of max number from to the right, we can iterate from right to left to calculate the remaining water
        # l is at the maximum but the end is open
        t, h = len(height) - 1, len(height) - 2
        if l != len(height) - 1:
            vol += ((t - l - 1)*height[t])
        while(h > l):
            if height[h] > height[t]:
                vol += ((h - l - 1)*height[h]) # with area with max

                vol -= (h-l)*height[t]

                t = h
            elif height[h] < height[t]:
                vol -= height[h]
            else:
                # when heights are equal
                vol -= height[h]
                t = h
            h-=1

        return vol