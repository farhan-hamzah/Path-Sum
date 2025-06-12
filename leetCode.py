# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: jika root kosong
        if not root:
            return False

        # Jika ini adalah node daun, periksa apakah path sum sesuai
        if not root.left and not root.right:
            return root.val == targetSum

        # Kurangi nilai node saat ini dari targetSum dan rekursi ke anak kiri dan kanan
        remainingSum = targetSum - root.val
        return (self.hasPathSum(root.left, remainingSum) or
                self.hasPathSum(root.right, remainingSum))
