class Solution(object):
    def sortSentence(self, s):
        val = [0,]*len(s.split())
        for i in s.split():
            text = i[:-1]
            index = int(i[-1])
            val[index-1] = text
            
        return ' '.join(val)
