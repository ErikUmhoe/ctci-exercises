from linked_list import Node
from stack import Stack

class MyQueue:
    def __init__(self, data=None):
        n = Node(data)
        self._first = Stack(n)
    def enqueue(self, data):
        self._first.push(data)

    def dequeue(self):
        temp_stk = Stack(self._first)
        last = None
        while self._first is not None:
            last = self._first.pop()
        return last