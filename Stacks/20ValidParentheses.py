class Solution:
    def isValid(self, s: str) -> bool:
        # Python stacks suck
        def peak(stack):
            if not stack:
                return None
            return stack[-1]
        
        validStart = ["(", "[", "{"]
        stack = []
        for i in range(len(s)):

            if s[i] in validStart:
                stack.append(s[i])
            else:
                if s[i] == ")" and peak(stack) == "(" or s[i] == "]" and peak(stack) == "[" or s[i] == "}" and peak(stack) == "{":
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False