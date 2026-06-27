class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i, n in enumerate(numbers):
            val = target - n
            if val in numbers:
                result = [numbers.index(val)+1, i+1]
        return result