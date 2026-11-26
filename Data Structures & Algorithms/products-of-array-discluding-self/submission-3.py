class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n

        # everything from left of i
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # everything from right of i
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # get the result
        for i in range(n):
            res[i] = prefix[i] * suffix[i]