# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Nested function kinda hit
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = defaultdict(list)
        def traverse(node, level=0):
            levels[level].append(node.val)
            level += 1
            if node.left:
                traverse(node.left, level)
            if node.right:
                traverse(node.right, level)
            return 
        traverse(root)
        return [sum(i)/len(i) for i in levels.values()]

