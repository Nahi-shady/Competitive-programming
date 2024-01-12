class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        left = 0
        anagram = Counter(p)
        window = Counter(s[:n-1])
        ans = []
        for i in range(n-1, len(s)):
            curr = s[i]
            window[curr] = window.get(curr, 0) + 1
            if window == anagram:
                ans.append(left)
            window[s[left]] -= 1
            left += 1

        return ans