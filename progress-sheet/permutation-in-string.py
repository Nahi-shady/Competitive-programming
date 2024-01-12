class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, n = 0, len(s1)
        freq1 = Counter(s1)
        freq2 = Counter(s2[:n-1])
        for i in range(n-1, len(s2)):
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
            
            if freq1 == freq2:
                return True
            freq2[s2[l]] -= 1
            l += 1

        return False