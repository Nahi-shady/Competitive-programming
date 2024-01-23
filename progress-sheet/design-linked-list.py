class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        dummy = self.head
        for _ in range(index):
            dummy = dummy.next
        
        return dummy.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            node = Node(val, self.head)
            self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        dummy = self.head
        while dummy.next:
            dummy = dummy.next
        dummy.next = Node(val)
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        dummy = self.head
        for _ in range(index-1):
            dummy = dummy.next
        curr = dummy.next
        dummy.next = Node(val, curr)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            dummy = self.head
            for _ in range(index-1):
                dummy = dummy.next
            dummy.next = dummy.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)