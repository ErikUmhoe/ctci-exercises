from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ht = {}
        ptr = head
        while ptr.next != None:
            if ptr.next in ht:
                return ptr.next
            ht[ptr] = ptr.next
            ptr = ptr.next
        return None
