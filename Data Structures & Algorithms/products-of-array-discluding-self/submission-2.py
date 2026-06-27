class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            product = 1
            if i == 0:
                for j in range(i+1, len(nums)):
                    product = product * nums[j]
                print('product', product)
                result[i] = product
                product = 1
            elif i == len(nums)-1:
                for j in range(0,i):
                    product = product*nums[j]
                result[i] = product
                product = 1
            else:
                prefix = 1
                postfix = 1
                j = 0
                for j in range(i):
                    prefix = prefix * nums[j]
                for j in range(i+1, len(nums)):
                    postfix = postfix * nums[j]
                result[i] = prefix * postfix
                i = i+1
        print('result', result)
        return result
                

        