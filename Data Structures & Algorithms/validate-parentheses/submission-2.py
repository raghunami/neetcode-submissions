class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(',
                    ']': '[',
                    '}': '{'
                    }
        stack = []

        for ch in s:
            if ch in brackets:
                if not stack:
                    return False
                top = stack.pop()
                if brackets[ch] != top:
                    return False
            else:
                stack.append(ch)
        return not stack



        