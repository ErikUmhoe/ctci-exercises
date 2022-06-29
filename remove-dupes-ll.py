from linked_list import LinkedList, Node
        
class Solution:
    def remove_dupes(self, linked: LinkedList):
        hashTable = {}
        trav = linked.head
        while trav != None or trav.next != None:
            hashTable[trav.data] = 1
            if trav.next.data in hashTable:
                trav.next = trav.next.next
            if trav.next == None:
                break
            trav = trav.next 
        return linked

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
sol.remove_dupes(ll)
print(ll)