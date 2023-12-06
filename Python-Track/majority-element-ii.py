from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        ans = [i for i, v in count.items() if v > n/3]
        
        return ans