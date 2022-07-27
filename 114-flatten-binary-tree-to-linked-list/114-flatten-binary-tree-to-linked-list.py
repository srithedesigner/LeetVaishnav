# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getPredess(self, root):
        
        node = root.left
        
        while node.right:
            node = node.right
        
        return node
    
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        if not root:
            return root
        
        node = root
        
        
        
        
        while node:
            if not node.left:
                node = node.right
                continue
            
            pred = self.getPredess(node)
            #print(pred.val)
            
            if not pred:
                node = node.right
                
            
            pred.right = node.right
            node.right = node.left
            x = node.left
            node.left = None
            
            node = x
        
        return
    
        