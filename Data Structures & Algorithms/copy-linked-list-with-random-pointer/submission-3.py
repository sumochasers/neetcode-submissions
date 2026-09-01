"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_to_new = {}

        node = head
        while node != None :
            
            if node not in old_to_new :
                newnode = Node(node.val)
                old_to_new[node] = newnode
            else:
                newnode = old_to_new[node]    

            random_node = node.random
            
            new_random_node = None
            
            if random_node : 
                if random_node not in old_to_new :
                    new_random_node = Node(random_node.val)
                    old_to_new[random_node] = new_random_node
                else:
                    new_random_node = old_to_new[random_node]  
            
            next_node = node.next

            new_next_node = None
            if next_node :
                if next_node not in old_to_new :
                    new_next_node = Node(next_node.val)
                    old_to_new[next_node] = new_next_node
                else:
                    new_next_node = old_to_new[next_node]

            
            newnode.next = new_next_node
            newnode.random = new_random_node

            node = node.next 

        return old_to_new[head] if head!= None else None

            
            

            

            


        