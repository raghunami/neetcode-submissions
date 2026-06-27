class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDups = set()
        for num in nums:
            if num in checkDups:
                return True
            checkDups.add(num)
        return False
