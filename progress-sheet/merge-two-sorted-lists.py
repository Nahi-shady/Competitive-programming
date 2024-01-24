# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        dummy = head = ListNode
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val < p2.val:
                dummy.next = p1
                dummy = dummy.next
                p1 = p1.next
            else:
                dummy.next = p2
                dummy = dummy.next
                p2 = p2.next

        if p1:
            dummy.next = p1
        if p2:
            dummy.next = p2 

        return head.next