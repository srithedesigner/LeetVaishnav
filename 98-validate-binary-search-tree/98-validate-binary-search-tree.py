# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, _min, _max):
            
            
            
            
            if root is None:
                return True
    
            if root.val >= _max or root.val <= _min:
                
                return False
            
            return validate(root.left, _min, root.val) and validate(root.right, root.val, _max)
        
            
        return validate(root, float('-inf'), float('inf'))