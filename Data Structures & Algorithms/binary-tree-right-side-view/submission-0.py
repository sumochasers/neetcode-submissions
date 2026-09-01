# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = deque()
        q.append(root)

        while q :
            que_len = len(q)
            right_view = None
            for i in range(que_len):
                node = q.popleft()
                if node :
                    right_view = node
                    if node.left :
                        q.append(node.left)
                    if node.right :
                        q.append(node.right)
            if right_view :
                res.append(right_view.val)
        
        return res

        