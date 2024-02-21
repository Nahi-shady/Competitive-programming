class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        n = len(w)
        
        neighbor = sorted([w[i] + w[i+1] for i in range(n-1)])
        return sum(neighbor[-k+1:])  - sum(neighbor[:k-1]) if k > 1 else 0