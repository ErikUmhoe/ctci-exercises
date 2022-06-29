# BST Properties
# Each node in tree has <= 2 children
# left child < parent
# right child > parent
# every sub tree in a BST is also a BST
# no duplicates
from min_tree import BNode

class BstFromArray:
    
    def createTree(self, sortedArray):  # [1,3,5,7,12,15,20,34]
        arrLen = len(sortedArray)
        if arrLen == 0:
            return None
        if arrLen == 1:
            return BNode(sortedArray[0])
        midIndex = arrLen // 2
        root = BNode(sortedArray[midIndex])
        root._l = self._createSubTree(root, sortedArray[0:midIndex])
        root._r = self._createSubTree(root, sortedArray[midIndex + 1:])
        return root
    def _createSubTree(self, root: BNode, subArray):
        if len(subArray) == 0:
            return root
        if len(subArray) == 1:
            root._l = BNode(subArray[0])
            return root
        if len(subArray) == 2:
            root._l = BNode(subArray[0])
            root._r = BNode(subArray[1])
            return root
        midIndex = len(subArray) // 2
        root._l = self._createSubTree(root, subArray[0:midIndex])
        root._r = self._createSubTree(root, subArray[midIndex + 1:])
    


        
    
    
            