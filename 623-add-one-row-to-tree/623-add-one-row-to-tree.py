# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        depth -= 1
        root = TreeNode(-1, root, None)
        q = deque()
        q.append(root)
        level = 0
        while len(q) != 0:

            n = len(q)

            for i in range(n):
                x = q.popleft()
                if level == depth:

                    
                    x.left = TreeNode(val, x.left, None)
                    x.right = TreeNode(val, None, x.right)
                
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            level += 1
        
        return root.left
