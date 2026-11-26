class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countsS1 = [0] * 26
        countsS2 = [0] * 26
        l = 0

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            countsS1[ord(s1[i]) - ord('a')] += 1
            countsS2[ord(s2[i]) - ord('a')] += 1

        for r in range(len(s1), len(s2)):
            if countsS1 == countsS2:
                return True

            # add character to right
            countsS2[ord(s2[r]) - ord('a')] += 1
            # remove character from left
            countsS2[ord(s2[l]) - ord('a')] -= 1

            l += 1

        return countsS1 == countsS2
