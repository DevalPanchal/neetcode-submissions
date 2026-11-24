# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. base case
        if not root:
            return 0

        # 2. get heights of left and right trees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # return 1 for every node visited plus the max of either left or right
        return 1 + max(left, right)