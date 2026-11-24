# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root:Optional[TreeNode]) -> Tuple[bool, int]:
        if not root:
            return (True, 0)
        lb, lh = self.helper(root.left)
        rb, rh = self.helper(root.right)
        return (lb and rb and abs(lh-rh)<=1, 1 + max(lh, rh))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root)[0]