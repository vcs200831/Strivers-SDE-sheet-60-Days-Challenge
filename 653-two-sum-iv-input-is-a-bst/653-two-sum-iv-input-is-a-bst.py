# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = set()
        def dfs(node):
            if not node: return 0
            
            y = k - node.val
            
            if y in l:
                return 1
            else:
                l.add(node.val)
                
            return dfs(node.left)  or dfs(node.right)
        return dfs(root)