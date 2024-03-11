class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order1 = Counter(order)
        order2 = Counter(s)
        ans = []

        for char, count in order1.items():
            if char in order2:
                ans.append(char*order2[char])
                order2.pop(char)
                
        for char, count in order2.items():
            ans.append(char*count)

        return ''.join(ans)