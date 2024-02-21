class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles and target > 1:
            r = target % 2
            target = (target // 2) 
            maxDoubles -= 1
            count += r + 1
        return count + target - 1
