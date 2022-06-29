from linked_list import Node
from stack import Stack

class Stack_Of_Stacks():
    def __init__(self, limit: int):
        self._first = None
        self._limit = limit
    def push(self, data):
        if self._limit == self._first._count:
            new_stack = Stack(data)
            self._first.next = new_stack._first
            self._first = new_stack._first
        else:
            self._first.push(data)
            self._first._count += 1
    def pop(self):
        return self._first.pop()
    def peek(self):
        return self._first.peek()