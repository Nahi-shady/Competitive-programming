class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left, curr, max_vowels = 0, 0, 0

        for i in range(k):
            if s[i] in vowels:
                max_vowels += 1
                curr += 1

        for r in range(k, len(s)):
            curr_s = s[r]
            if curr_s in vowels:
                curr += 1
            if s[left] in vowels:
                curr -= 1
            left += 1
            max_vowels = max(max_vowels, curr)
    
        return max_vowels