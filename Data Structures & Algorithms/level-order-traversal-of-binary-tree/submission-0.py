# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root :
            return []
        
        q = deque()
        q.append(root)

        res = []
        while len(q) != 0 :
            sublist = []
            for i in range(0,len(q)):
                node = q.popleft()
                sublist.append(node.val)
                if node.left != None :
                    q.append(node.left)
                if node.right != None :
                    q.append(node.right)
            res.append(sublist)    

        print(res)
        return res


        