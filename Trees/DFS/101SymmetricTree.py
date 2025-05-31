# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.valSame(root.left, root.right)
    
    def valSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p != None and q == None or p == None and q != None:
            return False 
        return p.val == q.val and self.valSame(p.left, q.right) and self.valSame(p.right, q.left)
