class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0]*(n+1)
        for l, r, shift in shifts:
            if shift == 0:
                prefix[l] -= 1
                prefix[r+1] += 1 
            else:
                prefix[l] += 1
                prefix[r+1] -= 1
        prefix = list(accumulate(prefix[:-1]))
        ans = []
        for i in range(n):
            asci = (ord(s[i])- 96 + prefix[i]) % 26
            if asci == 0:
                ans.append('z')
            else:
                ans.append(chr(asci+96))
        
        return ''.join(ans)