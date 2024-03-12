# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        prefix = 0
        dummy = head
        while dummy:
            if stack and stack[-1] + dummy.val == 0:
                top = stack.pop()
                prefix -= top
            elif prefix + dummy.val == 0:
                stack.clear()
                prefix = 0
            else:
                temp = []
                curr = 0
                while stack and curr + dummy.val != 0:
                    top = stack.pop()
                    curr += top
                    temp.append(top)
                if curr + dummy.val != 0:
                    for i in temp[::-1]:
                        stack.append(i)
                    prefix += dummy.val
                    stack.append(dummy.val)
                else:
                    prefix -= curr
                
            dummy = dummy.next
        if stack:
            head = ListNode(stack[0])
            dummy = head
            for i in range(1, len(stack)):
                dummy.next = ListNode(stack[i])
                dummy = dummy.next
            
            return head
        