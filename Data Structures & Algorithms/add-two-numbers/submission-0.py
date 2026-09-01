# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        current = dummy = ListNode()
        
        
        ptr1 = l1 
        ptr2 = l2 

        carry = 0 

        while ptr1 or ptr2 or carry :

            val1 = ptr1.val if ptr1   else 0
            val2 = ptr2.val if ptr2   else 0

            print(val1, "-", val2)
            total_sum = val1 + val2 + carry 
            quo = total_sum // 10
            remainder = total_sum % 10
            if quo :
                val = remainder
                carry = quo     
            else :
                val = remainder
                carry = 0 
            
            node = ListNode(val)
            current.next = node
            current = node

            if ptr1 :
                ptr1 = ptr1.next
            if ptr2 : 
                ptr2 = ptr2.next

        return dummy.next

