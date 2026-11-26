import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallestSpeed = 0
        largestSpeed = max(piles)

        while smallestSpeed < largestSpeed:
            mid = (smallestSpeed + largestSpeed) // 2

            hours = sum(math.ceil(pile/mid) for pile in piles)

            if hours <= h:
                largestSpeed = mid
            else:
                smallestSpeed = mid + 1

        return smallestSpeed