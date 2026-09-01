# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        
        prev = None
        while current :
            next = current.next 
            current.next = prev
            prev = current
            current = next
             
        n1 = head 
        n2 = prev

        while n2 :
            n1_next = n1.next
            n2_next = n2.next

            n1.next = n2
            n2.next = n1_next

            n1 = n1_next
            n2 = n2_next        



            
        
        
