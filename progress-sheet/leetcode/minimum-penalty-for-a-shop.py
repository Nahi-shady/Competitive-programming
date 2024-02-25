class Solution:
    def bestClosingTime(self, customers: str) -> int:
        j = -1
        score = 0
        maxScore = 0
        a = list(customers)
        
        for i in range(len(a)):
            if a[i] == 'Y':
                score += 1
            else:
                score -= 1
            
            if score > maxScore:
                j = i
                maxScore = score
        
        return j + 1