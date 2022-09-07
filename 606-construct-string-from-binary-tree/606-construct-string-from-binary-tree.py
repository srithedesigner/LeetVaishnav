# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        
        
        def preorder(node):
            
            if not node:
                return ""
            
            x = []
            x.append(str(node.val))
            
            if node.left or node.right:
                
                x.append("(")
                x.append(preorder(node.left))
                x.append(")")

            if node.right:
                x.append("(")
                x.append(preorder(node.right))
                x.append(")")
            
            return "".join(x)
        
        
        
        
        
        return preorder(root)
            
            
            