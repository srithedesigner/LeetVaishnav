class Solution(object):
    def lengthOfLongestSubstring(self, s):

        left = 0
        right = 0
        char_set = set()
        ans = 0
        while right < len(s):

            while left <= right and s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1

        return ans


        
