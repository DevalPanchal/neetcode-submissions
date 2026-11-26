class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
            
        # convert the map to a list of tuples
        result = list(frequency_map.items())

        # sort the list in reverse order
        result.sort(key=lambda pair: pair[1], reverse=True)

        # get list of counts only from tuples
        count_list = [pair[0] for pair in result]

        return count_list[:k]