# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs( self, node, minimum, maximum) :
        res = True
        if node.val > minimum and node.val < maximum :
            if node.left :
                res = self.dfs(node.left, minimum, node.val)

            if res and node.right :
                res = self.dfs(node.right, node.val, maximum)
        else :
            res = False
        
        return res
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

        