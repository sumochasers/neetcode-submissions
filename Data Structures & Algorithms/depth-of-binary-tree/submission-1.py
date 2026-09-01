# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None :
            return 0

        leftHeight = self.getHeight(root.left)    
        rightHeight = self.getHeight(root.right)

        return 1 + max(leftHeight,rightHeight)


    
    
    def getHeight(self, node) :

        if node == None :
            return 0
        return 1 + max (self.getHeight(node.left), self.getHeight(node.right))     