class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtractedMap = {}
        for i in range(len(nums)):
            subtractedValue = target - nums[i]

            if subtractedValue in subtractedMap:
                #print(subtractedMap)
                return [subtractedMap[subtractedValue], i]
            else:
                subtractedMap[nums[i]] = i