class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]:
                    return False
                
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
        
        return True