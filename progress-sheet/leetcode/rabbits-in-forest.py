class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key, val in count.items():
            if key == 0:
                ans += val
            elif val <= key + 1:
                ans += key + 1
            else:
                ans += ceil(val/(key+1)) * (key+1)
        return ans