class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        substring = set()
        n = len(s)
        left = 0
        right = 0
        while right < n:
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
                curr -= 1
            substring.add(s[right])
            curr += 1
            longest = max(longest, curr)
            right += 1
        return longest