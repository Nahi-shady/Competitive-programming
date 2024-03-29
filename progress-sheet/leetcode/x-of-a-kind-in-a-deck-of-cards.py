class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)
        # gcd = 
        
        for i in range(2, len(deck)):
            partition = all(not val%i for val in freq.values())
            if partition:
                return True

        if len(set(deck)) == 1 and len(deck) > 1:
            return True

        return False