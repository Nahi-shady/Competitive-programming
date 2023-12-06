class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        f, s, t = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        for word in words:
            if word[0].lower() in f:
                if all(i in f for i in word.lower()):
                    ans.append(word)
            elif word[0].lower() in s:
                if all(i in s for i in word.lower()):
                    ans.append(word)
            else:
                if all(i in t for i in word.lower()):
                    ans.append(word)
        return ans