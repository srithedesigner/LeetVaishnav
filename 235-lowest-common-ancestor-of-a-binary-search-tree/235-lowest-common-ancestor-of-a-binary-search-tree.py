# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find(root):
            
            if root is None:
                return None
            
            if root == p or root == q:
                return root
            
            if p.val < root.val < q.val:
                
                return root
            
            if q.val < root.val < p.val:
                
                return root
            
            if p.val < root.val and q.val < root.val:
                return find(root.left)
            
            return find(root.right)
        
        
        return find(root)
            
        