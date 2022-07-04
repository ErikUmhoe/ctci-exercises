# Definition for a binary tree node.
import queue
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ht = {}
        ht[0] = [root.val]
        if root.left:
            self._levelOrder(root.left, 1, ht)
        if root.right:
            self._levelOrder(root.right, 1, ht)
        result = []
        for k in ht:
            result.append(ht[k])
        return result
            
    def _levelOrder(self, node, level, ht):
        if level in ht:
            ht[level].append(node.val)
        else:
            ht[level] = [node.val]
        if node.left:
            self._levelOrder(node.left, level + 1, ht)
        if node.right:
            self._levelOrder(node.right, level + 1, ht)
                
root = TreeNode(0)
lOne = TreeNode(1)
rOne = TreeNode(2)
lTwo = TreeNode(3)
rTwo = TreeNode(4)
lTwo2 = TreeNode(5)
rTwo2 = TreeNode(6)
lOne.left = lTwo
lOne.right = rTwo
rOne.left = lTwo2
rOne.right = rTwo2
root.left = lOne
root.right = rOne
sol = Solution()
print(sol.levelOrder(root))

