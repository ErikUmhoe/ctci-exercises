# Definition for singly-linked list.
from typing import List, Optional
import math
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ctr = 0
        ptr = head
        ht = {}
        ht[ctr] = ptr
        while ptr.next != None:
            ctr += 1
            ptr = ptr.next
            ht[ctr] = ptr
        mid = ctr // 2
        return ht[mid]
    
