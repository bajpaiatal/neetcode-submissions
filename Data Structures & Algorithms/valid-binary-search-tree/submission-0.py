# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode], maxm: Optional[TreeNode], minm: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if maxm and root.val>=maxm.val:
            return False
        if minm and root.val<=minm.val:
            return False
        return self.helper(root.left, root, minm) and self.helper(root.right, maxm, root)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, None, None)