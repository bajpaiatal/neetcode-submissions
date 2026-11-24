# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return (0, 0)
        height = 0
        ld, lh = self.helper(root.left)
        rd, rh = self.helper(root.right)
        height = 1 + max(lh, rh)
        diameter = max(ld, rd, lh + rh + 1)
        return (diameter, height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.helper(root)[0]-1