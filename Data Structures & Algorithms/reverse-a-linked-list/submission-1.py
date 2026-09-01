# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
    
    head = node  
    if node.next :
        head = dfs(node.next)
        node.next.next = node
    node.next = None
    
    return head


'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def dfs(node):
            if node == None :
                return None

            head = node
            if node.next :
                head = dfs(node.next)
                node.next.next = node
            node.next = None

            return head  


        return dfs(head)          





        