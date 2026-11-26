class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            temp = []
            for x in range(i, i + k):
                temp.append(nums[x])

            res.append(max(temp))

        return res