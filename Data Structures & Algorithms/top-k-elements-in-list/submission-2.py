class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        checkFreq = defaultdict(int)
        bucket = [[] for i in range(len(nums)+1)]
        result = []
        for n in nums:
            checkFreq[n] += 1
        for freq, num in checkFreq.items():
            bucket[num].append(freq)
        
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result[-1::-1]
        return


        