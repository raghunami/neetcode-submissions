class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        check = defaultdict(int)
        window = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):

            check[s[right]] += 1

            max_freq = max(max_freq, check[s[right]])
            window = right -left + 1

            if window - max_freq > k:
                check[s[left]] -= 1
                left += 1

            window = right - left + 1
            result = max(result, window )

        return result
