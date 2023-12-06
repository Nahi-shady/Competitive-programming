class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = len(s)
        ans = [None]*t
        for i in range(t):
            ans[indices[i]] = s[i]
            
        return ''.join(ans)