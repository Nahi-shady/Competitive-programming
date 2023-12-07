class Solution:
    def totalMoney(self, n: int) -> int:
        num = 8
        j=1
        count=1
        sum=0
        for i in range(1,n+1):
            if i==num:
                num+=7
                count+=1
                j=count
            sum+=j
            j+=1
        return sum
        
