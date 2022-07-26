# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        @lru_cache(None)
        def search(root, x):
            
            if not root:
                return False
            
            if root == x:
                return True
            
            return search(root.left, x) or search(root.right, x)
        
        
        @lru_cache(None)
        def get(root, p, q):
            
            if not root:
                return root
            
            if root == p or root == q:
                return root
            
            if search(root.left, p) and search(root.right, q):
                return root
            if search(root.right, p) and search(root.left, q):
                return root
            
            x = get(root.left, p, q)
            y = get(root.right, p, q)
            
            return x if x else y
        
        return get(root, p, q)
            