# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        def merge(l1,l2):
            dummy =ListNode(0)
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                
                tail = tail.next

            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            
            return dummy.next
        
        while len(lists) >1:
            merge_list =[]
            for i in range(0, len(lists),2):

                list1 = lists[i]
                list2 = lists[i+1] if len(lists) > i+1 else None
                merge_list.append(merge(list1, list2))

            lists = merge_list
        return lists[0]