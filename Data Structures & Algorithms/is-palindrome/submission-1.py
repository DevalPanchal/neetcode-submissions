import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        # while left index is less than right index
        while left < right:
            # if left element is not alphabet than increase pointer
            while s[left].lower().isalnum() == False:
                left += 1

            # id right element is not alphabet than decrease pointer
            while s[right].lower().isalnum() == False:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True