# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        q = deque([root])

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

                if i == level_size - 1:
                    res.append(node.val)
        
        return res







