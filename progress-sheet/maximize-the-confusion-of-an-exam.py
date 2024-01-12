class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, max_ = 0, 0
        t, f = 0, 0
        
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                t += 1
            else:
                f += 1
            while min(t, f) > k:
                if answerKey[l] == 'T':
                    t -= 1
                else:
                    f -= 1
                l += 1
            max_ = max(max_, r-l + 1)

        return max_