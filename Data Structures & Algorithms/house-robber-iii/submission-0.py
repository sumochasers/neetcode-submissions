# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    cache = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        
        if not root :
            return 0
        if root in self.cache :
            return self.cache[root]
        current = root.val
        if root.left :
            current += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right :
            current += self.rob(root.right.left) + self.rob(root.right.right)

        self.cache[root] =  max(current , self.rob(root.left) + self.rob(root.right))
        return self.cache[root]
        
        
        