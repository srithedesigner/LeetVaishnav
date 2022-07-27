class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def getPredess(root):
            
            if not root:
                return root
            
            node = root.left
        
            
            while node and node.right and node.right != root:
                node = node.right
                
            return node
        
        
        res = []
        
        node = root
        
        while node:
            
            
            
            
            if not node.left:
                res.append(node.val)
                node = node.right
                
            else:
                
                pred = getPredess(node)
                
                if pred.right == node:
                    node = node.right
                    pred.right = None
                else:
                    res.append(node.val)
                    pred.right = node
                    node = node.left
                    
            
        return res