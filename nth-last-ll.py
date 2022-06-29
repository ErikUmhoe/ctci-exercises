from linked_list import LinkedList, Node

class Solution:
    def remove_nth_last_ll(self, ll: LinkedList, n: int):
        numNodes = 1
        ptr = ll.head
        while ptr.next != None:
            numNodes += 1
            ptr = ptr.next
        ptr = ll.head
        ctr = 1
        while ptr.next != None:
            ctr += 1
            if numNodes - ctr == n:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next

sol = Solution()
n1 = Node(5)
n2 = Node(1)
n3= Node(5)
n4 = Node(3)
n5 = Node(3)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
ll = LinkedList(n1)
# sol.nth_last_ll(ll, 2)
print(ll)               