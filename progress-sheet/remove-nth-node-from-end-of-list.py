class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return 
        i = 0
        slow = fast = head
        while fast and  i < n:
            fast = fast.next
            i += 1
        if not fast:
            return head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return head