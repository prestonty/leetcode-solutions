# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        return self.findPathSum(root, root.val, targetSum)

    def findPathSum(self, root: Optional[TreeNode], currentSum: int, targetSum: int) -> bool:
        if currentSum == targetSum and root.left == None and root.right == None:
            return True
        
        left = False
        right = False
        if root.left != None:
            left = self.findPathSum(root.left, currentSum + root.left.val, targetSum)
        if root.right != None:
            right = self.findPathSum(root.right, currentSum + root.right.val, targetSum)
        
        return left or right
        