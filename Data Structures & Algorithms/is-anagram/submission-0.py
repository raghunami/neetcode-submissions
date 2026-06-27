class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        hashsetS = {}
        hashsetT = {}
        for i in range(len(s)):
            hashsetS[s[i]] = hashsetS.get(s[i], 0) + 1
            hashsetT[t[i]] = hashsetT.get(t[i], 0) + 1
        for ch in hashsetS:
            if hashsetS[ch] != hashsetT.get(ch, 0):
                return False
        return True 