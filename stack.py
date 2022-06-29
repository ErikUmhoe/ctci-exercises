from linked_list import Node 

class Stack:
    def __init__(self, data=None):
        n = Node(data)
        self._first = n
        self._count = 1
    def pop(self):
        if self._first == None:
            raise IndexError("Unable to remove an item from an empty stack")
        popped = self._first
        self._first = self._first.next
        return popped

    def push(self, data):
        new_node = Node(data)
        new_node.next = self._first
        if self._first == None:
            new_node.min = new_node
        elif new_node.data < self._first.data:
            new_node.min = new_node
            self._first.min = new_node
        else:
            new_node.min = self._first
        self._count += 1
        self._first = new_node

    def peek(self):
        return self._first

    def min(self):
        return self._first.min

stk = Stack(5)
stk.push(1)
stk.push(11)
stk.push(4)
stk.pop()
stk.push(7)
stk.pop()
stk.pop()
print(stk.min().data)