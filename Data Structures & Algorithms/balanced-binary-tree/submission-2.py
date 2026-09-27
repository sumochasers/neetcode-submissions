# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    max_hd = 0
    def dfs(self, node : TreeNode | None) -> int :
        if not node :
            return 0
        
        left_h = self.dfs(node.left)
        right_h = self.dfs(node.right)
        
        self.max_hd = max(self.max_hd, abs(left_h - right_h))

        return 1 + max(self.dfs(node.left), self.dfs(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.max_hd <= 1

        

       

        