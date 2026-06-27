class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set()
        result = 0
        for n in nums:
            numberSet.add(n)
        
        # for i in range(len(nums)):
        #     if (nums[i]-1) not in numberSet:
        #         j = nums[i]
        #         while(j in numberSet):
        #             j +=1
        #         result = max(result, j-nums[i])
        # return result
        for n in nums:
            if (n-1) not in numberSet:
                length = 0 
                while (n+length) in numberSet:
                    length += 1
                result = max(result, length)
        return result

        