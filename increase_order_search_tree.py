import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        h = []
        self._rearrange(root, h)
        newRoot = TreeNode(heapq.heappop(h))
        ptr = newRoot
        while len(h) > 0:
            tmp = heapq.heappop(h)
            ptr.left = None
            ptr.right = TreeNode(tmp)
            ptr = ptr.right
        return newRoot
            
        
    def _rearrange(self, node, h):
        if node.right:
            self._rearrange(node.right, h)
        heapq.heappush(h, node.val)
        if node.left:
            self._rearrange(node.left, h)