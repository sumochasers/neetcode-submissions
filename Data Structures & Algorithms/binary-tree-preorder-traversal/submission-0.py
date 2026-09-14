# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _preorder(self, node : Optional[TreeNode], res : list[int]) -> None :
        if not node :
            return
        res.append(node.val)
        self._preorder(node.left, res)
        self._preorder(node.right, res)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self._preorder(root, res)
        return res
        