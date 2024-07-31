# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Initial Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ldepth, rdepth = 0, 0
        if root.left:
            ldepth += Solution.maxDepth(Solution, root.left)
        if root.right:
            rdepth += Solution.maxDepth(Solution, root.right)
        return max(ldepth,rdepth) + 1
    
#Solution when I relized i could cut half of it
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ldepth = Solution.maxDepth(Solution, root.left)
        rdepth = Solution.maxDepth(Solution, root.right)
        return max(ldepth,rdepth) + 1