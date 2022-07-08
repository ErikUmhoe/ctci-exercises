# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.val == targetSum:
            return True
        return self._dfsSum(root, targetSum, 0)
        
    def _dfsSum(self, node, targetSum, runningSum):
        if runningSum + node.val == targetSum:
            return True
        if node.left:
            return self._dfsSum(node.left, targetSum, runningSum + node.val)
        if node.right:
            return self._dfsSum(node.right, targetSum, runningSum + node.val)
        