# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree. 
# 
#  A height-balanced binary tree is a binary tree in which the depth of the two 
# subtrees of every node never differs by more than one. 
# 
#  
#  Example 1: 
#  
#  
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
#  
# 
#  Example 2: 
#  
#  
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums is sorted in a strictly increasing order. 
#  
# 
#  Related Topics Array Divide and Conquer Tree Binary Search Tree Binary Tree ?
# ? 7605 \U0001f44e 392


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        
        def make_tree(left=0, right=len(nums)-1):
            if left > right:
                return None

            mid = (left + right) // 2

            treeNode = TreeNode(nums[mid], make_tree(left, mid - 1), make_tree(mid + 1, right))
            return treeNode

        return make_tree()

# leetcode submit region end(Prohibit modification and deletion)
