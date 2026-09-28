# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    res = 0
    def dfs(self, node : TreeNode, path_max : int) -> None :
        if node == None :
            return
        if node.val >= path_max :
            self.res += 1
        cur_max = max(path_max, node.val)
        self.dfs(node.left, cur_max)
        self.dfs(node.right, cur_max)


    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, float('-inf'))
        return self.res
        