# Given an array of unique integers, arr, where each integer arr[i] is strictly 
# greater than 1. 
# 
#  We make a binary tree using these integers, and each number may be used for 
# any number of times. Each non-leaf node's value should be equal to the product 
# of the values of its children. 
# 
#  Return the number of binary trees we can make. The answer may be too large 
# so return the answer modulo 10⁹ + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2] 
# 
#  Example 2: 
# 
#  
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 
# 5], [10, 5, 2]. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 1000 
#  2 <= arr[i] <= 10⁹ 
#  All the values of arr are unique. 
#  
# 
#  Related Topics Array Hash Table Dynamic Programming \U0001f44d 2139 \U0001f44e 169


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numFactoredBinaryTrees(self, arr):

        s = set(arr)

        @lru_cache(None)
        def total_ways(x):

            ans = 1

            for i in s:
                if x % i == 0 and x // i in s:
                    ans += (total_ways(i) * total_ways(x // i))

            return ans

        aks = 0
        for i in arr:
            aks += total_ways(i)
        return aks%(1000000000 + 7)
# leetcode submit region end(Prohibit modification and deletion)
