class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n, l, = len(cards), 0
        min_ = n
        window = set()
        if len(set(cards)) == n:
            return -1
        for r in range(n):
            while cards[r] in window:
                min_ = min(min_, r-l+1)
                window.discard(cards[l])
                l += 1
            window.add(cards[r])
            
        return min_