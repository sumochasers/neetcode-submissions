"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node :
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque([node])

        while len(q) != 0 :
            
            current_node = q.popleft()
            
            for nb in current_node.neighbors :
                
                if nb not in old_to_new : 
                    newNode =  Node(nb.val)
                    old_to_new[nb] = newNode
                    q.append(nb)
                
                old_to_new[current_node].neighbors.append(old_to_new[nb])
                

        
        return  old_to_new[node]       







