class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        freq = {'(': 0,
                ')': 0,
                }
        for i in s:
            if i == '(':
                freq['('] += 1
                count += freq[')']
                freq[')'] = 0
            else:
                if freq['(']:
                    freq['('] -= 1
                else:
                    freq[')'] += 1
        return count + freq['('] + freq[')']