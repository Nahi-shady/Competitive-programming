class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total, n= sum(cardPoints), len(cardPoints)
        curr_sum = sum(cardPoints[:n-k])
        max_sum = total - curr_sum
        for r in range(n-k, n):
            curr_sum += cardPoints[r]
            curr_sum -= cardPoints[r-(n-k)]
            
            max_sum = max(max_sum, total - curr_sum)

        return max_sum