class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # break early, i, j, k would never = 0
            if nums[i] > 0:
                break

            # skip look if same number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]

                if total == -nums[i]:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total > -nums[i]:
                    right -= 1
                else:
                    left += 1
        
        return res

