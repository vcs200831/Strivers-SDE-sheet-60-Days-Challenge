# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
            q = [root]
            
            answer = []
            
            while len (q) > 0:
                
                size  = len(q)
                
                sum = 0
                
                for i in range(size):
                    
                    node = q.pop(0)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                        
                    sum += node.val
                    
                average = sum/size
                
                answer.append(average)
                
            return answer
                