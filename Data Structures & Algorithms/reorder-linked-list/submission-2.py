# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 4 6 7 



1 7 2 6 3 4
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        nodes = []
        current = head
        while current :
            nodes.append(current)
            current = current.next
    
        l = 0 
        r = len(nodes) - 1
        
        while l < r :
            nodes[l].next = nodes[r]
            l += 1
            if l == r :
                break
            nodes[r].next = nodes[l]
            r -= 1
        nodes[l].next = None

        
        
