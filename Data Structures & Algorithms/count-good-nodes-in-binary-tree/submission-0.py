# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        
        def dfs(root, high):
            if not root:
                return  
            
            if root.val >= high :
                nonlocal count
                count += 1
            high = max(root.val, high)
            
            dfs(root.left, high)
            dfs(root.right, high)
        
        dfs(root, root.val)
        return count