class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs[0]) < 2:
            if strs == sorted(strs):
                return 0
            else:
                return 1

        count = 0
        i = 0
        while i < len(strs[0]):
            j = 1
            while j < len(strs):
                if ord(strs[j-1][i]) > ord(strs[j][i]):
                    count += 1
                    j = 1
                    break
                j += 1
            i += 1
        return count
            