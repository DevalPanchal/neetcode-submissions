# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = deque([root])

        while q:
            level_size = len(q)
            level = []

            for i in range(level_size):
                node = q.popleft()

                level.append(node.val)

                # handle left side
                if node.left is not None:
                    q.append(node.left)

                # handle right side
                if node.right is not None:
                    q.append(node.right)
            res.append(level)

        return res






