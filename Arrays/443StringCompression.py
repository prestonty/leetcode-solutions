class Solution:
    def compress(self, chars: List[str]) -> int:
        prevChar = ""
        p = 0 # tracks end index of compressed array (its the past)
        count = 1

        for i in range(len(chars)):
            if chars[i] != prevChar and count == 1:
                prevChar = chars[i]
                chars[p] = chars[i]
                p+=1
            elif chars[i] != prevChar:
                # put put each digit in count into array
                for j in range(len(str(count))):
                    chars[p+j] = str(count)[j]
                
                p+=(len(str(count))) # move to new one
                count = 1
                chars[p] = chars[i]
                prevChar = chars[i]
                p+=1

            elif chars[i] == prevChar and i == len(chars) - 1:
                count += 1
                for j in range(len(str(count))):
                    chars[p+j] = str(count)[j]
                
                p+=(len(str(count)))
            elif chars[i] == prevChar:
                count+=1

        return p

