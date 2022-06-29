from linked_list import Node
class SearchNode:
    def __init__(self, data=None):
        self._data = data
        self._visited = False
        self._children = []
    def addKid(self, node):
       self._children.append(node)
