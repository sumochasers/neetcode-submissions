# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # prev = None
        # current = head 
        # while current :
        #     next_ = current.next 
        #     current.next = prev
        #     prev = current
        #     current = next_
        # return prev
        
        dummy = ListNode(0,head)
        leftprev = dummy 

        for i in range(left - 1):
            leftprev = leftprev.next

        current = leftprev.next
        prev = None
        for i in range(right - left + 1):
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        
        leftprev.next.next = current
        leftprev.next = prev
        return dummy.next
            

            
             






        