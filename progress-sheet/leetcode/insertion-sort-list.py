class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy = ListNode(-float('inf'), head)
        curr = dummy.next
        while curr and curr.next:
            next = curr.next
            if curr.val > next.val:
                left = dummy
                while left.next and left.next.val < next.val:
                    left = left.next
                right = left.next
                curr.next = next.next
                next.next = right
                left.next = next
                curr = right
            else:
                
                curr = curr.next

        return dummy.next
            