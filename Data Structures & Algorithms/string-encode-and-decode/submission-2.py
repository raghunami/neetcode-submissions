class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_length = int(s[i:j])
            i = j+1
            decoded.append(s[i:i+str_length])
            i += str_length
        return decoded
