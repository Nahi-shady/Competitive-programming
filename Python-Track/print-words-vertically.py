class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxl = len(max(s, key=len))
        ans = [""]*maxl
        for i in s:
            p = 0
            while p < maxl:
                if p < len(i):
                    ans[p] += i[p]
                else:
                    ans[p] += ' '
                p += 1
        
        return [a.rstrip() for a in ans]