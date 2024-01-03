class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        n = len(skill)
        team = n//2                      
        desired = total // team       
        skill.sort()
        chem = 0
        l = 0       
        r = n-1
        while l<r:
            if skill[l] + skill[r] == desired:
                chem += skill[l]*skill[r]
            else:
                return -1
            l+=1
            r-=1
        return chem