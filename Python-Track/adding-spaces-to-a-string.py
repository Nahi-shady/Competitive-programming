class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modified = ''
        left = 0
        for i in spaces:
            modified += s[left:i] + ' '
            left = i

        return modified + s[i:]