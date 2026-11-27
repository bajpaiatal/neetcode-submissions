# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, idx: int, pre: List[int], mp_in: Dict[int, int], low: int, high: int) -> Tuple[Optional[TreeNode], int]:
        if idx >= len(pre) or low>high:
            return (None, idx)
        root = TreeNode(pre[idx])
        idx += 1
        mid = mp_in[root.val]
        root.left, idx = self.helper(idx, pre, mp_in, low, mid-1)
        root.right, idx = self.helper(idx, pre, mp_in, mid+1, high)
        return (root, idx)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp_in = {val:i for i,val in enumerate(inorder)}
        return self.helper(0, preorder, mp_in, 0, len(preorder)-1)[0]