class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        odd = False
        for val in freq.values():
            if val % 2:
                ans += val-1
                odd = True
            else:
                ans += val
        return ans + 1 if odd else ans
