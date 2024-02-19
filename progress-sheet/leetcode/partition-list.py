class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        l_tail = left
        right = ListNode()
        r_tail = right
        dummy = head
        while dummy:
            if dummy.val < x:
                l_tail.next = ListNode(dummy.val)
                l_tail = l_tail.next
            else:
                r_tail.next = ListNode(dummy.val)  
                r_tail = r_tail.next
            
            dummy = dummy.next
            
        l_tail.next = right.next 
        return left.next