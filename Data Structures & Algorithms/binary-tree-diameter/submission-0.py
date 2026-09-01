# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root == None :
            return 0
        
        leftH = self.maxHeight(root.left)
        rightH = self.maxHeight(root.right)

        diameter = leftH + rightH

        sub = max( self.diameterOfBinaryTree(root.left), 
                   self.diameterOfBinaryTree(root.right))

        return max(diameter,sub)


        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return total

    def maxHeight(self, root):

        if root == None :
            return 0

        return 1 + max(self.maxHeight(root.left),self.maxHeight(root.right))



        