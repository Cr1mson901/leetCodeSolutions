# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Not the greatest
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        swap = root.left
        root.left = root.right
        root.right = swap
        if root.right:
            Solution.invertTree(Solution,root.right)
        if root.left:
            Solution.invertTree(Solution,root.left)
        return root

#Apparently going down first is faster for some reason
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        if root.right:
            Solution.invertTree(Solution,root.right)
        if root.left:
            Solution.invertTree(Solution,root.left) 
        swap = root.left
        root.left = root.right
        root.right = swap
        return root