# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        while curr and curr.next:
            nxt = curr.next
            new = ListNode(math.gcd(curr.val, nxt.val))
            curr.next = new
            new.next = nxt

            curr = nxt
        return head