"""
Given a Binary Tree, find the sum of all left leaves in it.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_of_left_leaves(self, root: TreeNode) -> int:
        self.total = 0

        def dfs(node, left):
            if not node:
                return

            dfs(node.left, True)
            dfs(node.right, False)

            if not node.left and not node.right and left:
                self.total += node.val

        dfs(root, False)

        return self.total
