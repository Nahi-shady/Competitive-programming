class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hash = {}

        for match in matches:
            if match[0] in hash:
                hash[match[0]][0] += 1
            else:
                hash[match[0]] = [1, 0]
            
            if match[1] in hash:
                hash[match[1]][1] += 1
            else:
                hash[match[1]] = [0, 1]
                
        no_loss = []
        lost_1 = []
        for idx, val in hash.items():
            if val[1] == 0:
                no_loss.append(idx)
            elif val[1] == 1:
                lost_1.append(idx)
         
        return [sorted(no_loss), sorted(lost_1)]