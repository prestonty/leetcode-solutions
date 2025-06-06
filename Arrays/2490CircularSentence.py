class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(" ")

        # check first case - first word and last word in sentence
        if arr[0][0] != arr[len(arr) - 1][len(arr[len(arr) - 1]) - 1]:
            return False
        for i in range(len(arr) - 1):
            if arr[i][len(arr[i]) - 1] != arr[i+1][0]:
                return False
        
        return True