# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        total =0
        curr = head

        while curr:
            total +=1
            curr = curr.next
        
        dummy =ListNode(0)
        dummy.next = head

        beforestart = dummy

        while total >= k:
            
            start = beforestart.next
            prev =None
            curr = start

            for i in range(k):
                nxt = curr.next 
                curr.next = prev
                prev = curr
                curr = nxt

            beforestart.next = prev
            start.next = curr
            beforestart = start

            total -=k
        return dummy.next
