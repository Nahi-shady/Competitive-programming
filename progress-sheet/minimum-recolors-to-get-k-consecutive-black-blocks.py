class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, n, min_ = 0, len(blocks), float('inf')
        operations = 0
        for i in range(n):
            if blocks[i] == 'W':
                operations += 1
            if i >= k-1:
                min_ = min(min_, operations)
                if blocks[l] == 'W':
                    operations -= 1

                l += 1

        return min_