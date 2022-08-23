# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseLinkedList(head):
            
            prev = None
            curr = head
            n_ext = None
            
            while curr:
                
                n_ext = curr.next
                curr.next = prev
                prev = curr
                
                curr = n_ext
            
            return prev
        
        return reverseLinkedList(head)