# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = n = ListNode()
        
        while list1 != None and list2 != None :
            
            if list1.val < list2.val :
                n.next = list1
                n = list1
                list1 = list1.next
            else :
                n.next = list2
                n = list2
                list2 = list2.next 

        n.next = list1 or list2

        return dummy.next



            


                  
             



        