from linked_list import LinkedList, Node

class Solution:
    def remove_middle(self, midNode: Node): 
        if midNode.next == None:
            midNode = None
        midNode.data = midNode.next.data
        midNode.next = midNode.next.next

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
sol.remove_middle(n3)
print(ll)