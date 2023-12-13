class Solution:
    def isHappy(self, n: int) -> bool:
        summation = n
        impossible = (2, 4, 16, 37, 58, 89, 145, 42)
        while summation != 1:
            if summation in impossible:
                return False
            summation = sum([int(i)*int(i) for i in str(summation)])
        
        return True