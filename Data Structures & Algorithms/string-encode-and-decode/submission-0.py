class Solution:

    def encode(self, strs: List[str]) -> str:
        '''encodes string by length delimiter like URL'''
        encoded_string = []
        for s in strs:
            encoded_string.append(f"{len(s)}#{s}")
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        '''decodes string into list of strings'''
        res = []
        i = 0

        while i < len(s):
            # find where delimiter # ends for current string
            j = i
            while s[j] != '#':
                j += 1

            # extract the length of the string
            length = int(s[i:j])

            # actual string starts right after # and spans length
            start_idx = j + 1
            end_idx = start_idx + length
            res.append(s[start_idx:end_idx])

            # move pointer to the start of the next encoded block
            i = end_idx

        return res