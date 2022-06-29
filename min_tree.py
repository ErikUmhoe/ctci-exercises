from queue import Queue
from linked_list import Node

class BNode:
    def __init__(self, value):
        self._l = None
        self._r = None
        self._value = value
        self._marked = False
    
class BTree:
    def __init__(self):
        self._root = None

    def getRoot(self):
        return self._root
    
    def add_to_tree(self, value):
        if self._root == None:
            self._root = BNode(value)
        else:
            self._add(value, self._root)

    def _add(self, value: int, node: BNode):
        if value < node._value:
            if node._l is not None:
                self._add(value, node._l)
            else:
                node._l = BNode(value)
        else:
            if node._r is not None:
                self._add(value, node._r)
            else:
                node._r = BNode(value)

    def pre_order_traversal(self):
        if self._root is not None:
            self._pre_order(self._root)
            
    def _pre_order(self, node: BNode):
        print(str(node._value) + ' ')
        if node._l:
            self._pre_order(node._l)
        if node._r:
            self._pre_order(node._r)

    def in_order_traversal(self):
        if self._root is not None:
            self._in_order(self._root)

    def _in_order(self, node: BNode):
        if node._l is not None:
            self._in_order(node._l)
        print(str(node._value))
        if node._r is not None:
            self._in_order(node._r)
        
    def post_order_traversal(self):
        if self._root:
            self._post_order(self._root)
    
    def _post_order(self, node: BNode):
        if node._l:
            self._post_order(node._l)
        if node._r:
            self._post_order(node._r)
        print(str(node._value))




    # def remove_from_tree(self, value):

# tree = BTree()
# tree.add_to_tree(3)
# tree.add_to_tree(4)
# tree.add_to_tree(7)
# tree.add_to_tree(5)
# tree.add_to_tree(8)
# tree.pre_order_traversal()
# print()
# tree.in_order_traversal()
# print()
# tree.post_order_traversal()
# print()
# print(tree.getRoot()._value)