# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Too many if statments for my liking
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        if not Solution.isSameTree(Solution,p.left,q.left):
            return False
        if not Solution.isSameTree(Solution,p.right,q.right):
            return False
        return True
    
#Removed one of the if statements. Gotta love try
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        try:
            if p.val != q.val:
                return False
        except:
            return False
        if not Solution.isSameTree(Solution,p.left,q.left):
            return False
        if not Solution.isSameTree(Solution,p.right,q.right):
            return False
        return True