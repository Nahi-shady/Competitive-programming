class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i+j].append(mat[i][j])
            
        ans = []
        for key, val in diagonals.items():
            if key % 2 != 0:
                ans += val
            else:
                ans += val[::-1]

        return ans