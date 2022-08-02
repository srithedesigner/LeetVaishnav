import bisect


class Solution(object):
    def kthSmallest(self, matrix, k):

        low = matrix[0][0]
        high = matrix[-1][-1]
        ans = float('inf')
        while low <= high:

            mid = low + (high - low)//2
            #print(low, mid, high)
            pos = 0
            for row in matrix:
                pos += bisect.bisect_right(row, mid)

            #print(mid, pos)

            if pos == k:
                ans = min(ans, mid)
                high = mid - 1

            elif pos > k:
                ans = min(ans, mid)
                high = mid - 1
            else:

                low = mid + 1

        return ans
