from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = defaultdict(int)
        for i in range(len(list1)):
            if list1[i] in list2:
                count[list1[i]] += i + list2.index(list1[i])
        
        minimum = min(count.values())
        return [i for i, v in count.items() if v == minimum]
