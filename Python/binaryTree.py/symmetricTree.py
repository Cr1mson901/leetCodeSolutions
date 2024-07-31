# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#This is the 2nd ugliest code Ive ever made
class Solution:
    def isSymmetric(self, root: Optional[TreeNode], root2=None, first=True) -> bool:
        if first:
            root2 = root
            first = False
        if (not root and root2) or (not root2 and root):
            return False
        if type(root) == type(root2) and not root:
            return True
        if root.val != root2.val:
            return False
        elif not root or not root2:
            return False
        return (self.isSymmetric(root.left, root2.right, first) and self.isSymmetric(root.right, root2.left,first))