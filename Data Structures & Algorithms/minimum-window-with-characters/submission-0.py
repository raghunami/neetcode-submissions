class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        window_count = {}

        left = 0
        result = ""
        have = 0

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1
        
        need = len(t_count)

        for right in range(len(s)):
            window_count[s[right]] = window_count.get(s[right], 0) + 1

            if s[right] in t_count and window_count[s[right]] == t_count[s[right]]:
                have += 1

            while have == need:
                if result == "" or (right - left + 1) < len(result):
                    result = s[left:right+1]

                window_count[s[left]] -= 1

                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                
                left +=1 

        return result






        