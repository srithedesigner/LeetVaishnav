# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ret = []
        
        def getPredess(root):
            
            node = root.left
            
            while node.right and node.right != root:
                
                node = node.right
                
            return node
            
        
        
        def inorder(root):
            
            node = root
            
            
            if not root:
                return
                
                
            while node:
                
            
            
                if not node.left:

                    ret.append(node.val)
                    node = node.right
                
                else:
                    predess = getPredess(node)
                    
                    if predess.right == node:
                        
                        ret.append(node.val)
                        predess.right = None
                        node = node.right
                    
                    else:
                        predess.right = node
                        node = node.left
                        
        inorder(root)
        
        return ret