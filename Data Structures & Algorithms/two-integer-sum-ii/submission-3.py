class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            # decrease right pointer if target larger
            if numbers[left] + numbers[right] > target:
                right -=1  

            # increase left pointer if target is smaller
            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            