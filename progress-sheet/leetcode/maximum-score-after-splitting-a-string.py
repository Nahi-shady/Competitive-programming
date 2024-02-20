class Solution:
    def maxScore(self, s: str) -> int:
        arr = [int(i) for i in s]
        tot = sum(arr)
        zeros = 0
        ans = 0
        for i in arr[:-1]:
            if i == 0:
                zeros += 1
            else:
                tot -= 1
            ans = max(ans, tot + zeros)
            print(zeros, tot)
        
        return ans