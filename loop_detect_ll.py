from linked_list import LinkedList, Node

class Solution:
    def detect_loop(self, ll: LinkedList):
        ptr = ll.head
        hashTable = {}
        while ptr.next != None:
            if ptr.data in hashTable and ptr == hashTable[ptr.data]:
                return hashTable[ptr.data]
            hashTable[ptr.data] = ptr
            ptr = ptr.next
        return None

sol = Solution()
n1 = Node(5)
n2 = Node(1)
n3= Node(2)
n4 = Node(3)
n5 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
ll = LinkedList(n1)
print(sol.detect_loop(ll))