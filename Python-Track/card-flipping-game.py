class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        set_ = set(fronts + backs)

        for f,b in zip(fronts, backs):
            if f == b:
                set_.discard(f)
        
        return min(set_, default = 0)