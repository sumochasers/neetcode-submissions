# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs( self, node, minimum, maximum) :
        if not node :
            return True
        if node.val <= minimum or node.val >= maximum :
            return False
        
        left_status = self.dfs(node.left, minimum, node.val)
        right_status = self.dfs(node.right, node.val, maximum)
        
        return (left_status and right_status)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

        