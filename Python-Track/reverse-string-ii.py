class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sentence = ""
        for x in range(0, len(s), k+k):
            word = s[x:x+k+k]
            sentence += word[0:k][::-1]
            sentence += word[k:] 
            
        return sentence