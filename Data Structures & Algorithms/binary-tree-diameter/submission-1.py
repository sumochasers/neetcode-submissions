# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    max_diameter = 0
    def dfs(self, node : TreeNode | None) -> int :
        if not node :
            return 0
        
        left_h = self.dfs(node.left)
        right_h = self.dfs(node.right)
        self.max_diameter = max(self.max_diameter, left_h + right_h)

        return 1 + max(left_h, right_h)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_diameter


        