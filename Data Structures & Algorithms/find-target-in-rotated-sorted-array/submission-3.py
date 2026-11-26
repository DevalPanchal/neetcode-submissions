class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. find minimum
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        # 2. find which side target is on
        pivot = low

        if nums[pivot] <= target <= nums[len(nums) - 1]:
            low = pivot
            high = len(nums) - 1
        else:
            low = 0
            high = pivot - 1
        
        # 3. binary search
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1