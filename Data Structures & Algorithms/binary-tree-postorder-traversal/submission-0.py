# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _postorder(self, node : Optional[TreeNode], res : list[int]) -> None :
        if not node :
            return
        self._postorder(node.left, res)
        self._postorder(node.right, res)
        res.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self._postorder(root, res)
        return res