class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        left = 0
        window_len = 0
        longest  = 0


        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left += 1

            window_len = (right - left) + 1
            longest = max(longest, window_len)
            check.add(s[right])
        
        return longest


        