# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode, maxVal: int) -> int:
        if not root:
            return 0
        res = 0
        if root.val>=maxVal:
            res += 1
        maxVal = max(root.val, maxVal)
        res += self.dfs(root.left, maxVal)
        res += self.dfs(root.right, maxVal)
        return res

    def goodNodes(self, root: TreeNode) -> int:
        # 2 1 3
        if not root:
            return 0
        return self.dfs(root, root.val)