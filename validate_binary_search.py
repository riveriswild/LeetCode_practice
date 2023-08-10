# Given the root of a binary tree, determine if it is a valid binary search tree. 
# A valid BST is defined as follows:
#     - the left subtree of a node contains only nodes with keys less than the node's key 
#     - the right subtree of a node contains only nodes with keys greater than the node's key
#     - both the left and right subtrees must also be binary search trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def helper(self, root, left, right):
        if root is None:  # reached the end 
            return True
        if not (left < root.val < right):
            return False
        return self.helper(root.left, left, root.val) and self.helper(root.right, root.val, right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
    
    '''
                  5
              /   |  \
            /          \
            1            6
            |          / | \
                     4      3
                     |      |
    '''
    helper(root=5, left='-inf', right='inf')
    self.helper(root.left=1, left='-inf', root.val=5) and self.helper(root.right=6, root.val=5, right="inf")