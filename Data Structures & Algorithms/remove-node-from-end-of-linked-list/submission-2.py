# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        '''
        dummy = ListNode(0,head)
        right = head
        left = dummy
        

        while n > 0 :
            right = right.next
            n -= 1

        while right != None :
            right = right.next
            left = left.next


        left.next = left.next.next
        return dummy.next
        '''        
        node = head
        length_of_list = 0
        while node != None :
            node = node.next
            length_of_list += 1

        delete_position = length_of_list - n 
        

        node = head

        if delete_position == 0 :

            return node.next 

        for i in range (length_of_list) :
            
            if delete_position == i+1 :
                node.next = node.next.next
                break
            
            node = node.next    

        return head



            




        