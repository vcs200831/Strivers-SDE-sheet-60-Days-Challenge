# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,maxmVal):
            if not node:
                return 0
            
            result = 1 if node.val >= maxmVal else 0
            
            maxmVal = max(maxmVal,node.val)
            
            result += dfs(node.left,maxmVal)
            
            result += dfs(node.right,maxmVal)
            
            return result
        
        return dfs(root,root.val)
            
            
                          
                          
            
            