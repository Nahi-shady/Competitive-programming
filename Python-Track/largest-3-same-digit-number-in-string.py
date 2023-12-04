class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = ''
        curr = num[0]
        print(num[1:])
        for i in num[1:]:
            if i == curr[0]:
                curr += i
            else:
                curr = i
            if len(curr) == 3:
                good = max(curr, good)
                
        return good