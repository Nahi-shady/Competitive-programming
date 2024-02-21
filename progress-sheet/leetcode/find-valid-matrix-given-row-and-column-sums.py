class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = []
        n = len(rowSum)
        m = len(colSum)
        for i in range(n):
            row = []
            for j in range(m):
                x = min(rowSum[i], colSum[j])
                row.append(x)
                rowSum[i] -= x
                colSum[j] -= x
            matrix.append(row)

        return matrix