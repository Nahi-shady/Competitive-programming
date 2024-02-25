class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        window = 0
        
        for i, char in enumerate(s):
            d[char] = d.get(char, 0) + 1
            if window+1 - max(d.values()) <= k:
                window += 1
            else:
                d[s[i-window]] -= 1
        
        return window
        
  