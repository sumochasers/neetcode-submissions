# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _inorder(self, node : Optional[TreeNode], res : list[int]) -> None :
        if not node :
            return
        self._inorder(node.left, res)
        res.append(node.val)
        self._inorder(node.right, res)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self._inorder(root, res)
        return res

        
        
        