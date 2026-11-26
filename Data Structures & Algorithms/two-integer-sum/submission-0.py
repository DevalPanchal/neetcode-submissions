class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        retval = []

        for i, num in enumerate(nums):
            x = target - num
            if x in seen:
                retval.append(seen[x])
                retval.append(i)
                break
            seen[num] = i

        return retval
