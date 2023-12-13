class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        summation = n

        while summation != 1:
            if summation in visited:
                return False

            visited.add(summation)
            summation = sum(int(i)**2 for i in str(summation))
        
        return True