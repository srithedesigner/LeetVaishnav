# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
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
        
        
       
        slow = head
        fast = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
        
        
        
        first = head
        second = slow
        
        
        
        reversed_second = reverseLinkedList(second)
        
    
        while first and reversed_second and first != reversed_second:
            
            if first.val != reversed_second.val:
                return False
            
            first = first.next
            reversed_second = reversed_second.next
        
        return True
        
            