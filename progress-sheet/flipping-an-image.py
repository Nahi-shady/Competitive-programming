class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in image:
            i, j = 0, len(row)-1
            
            while i <= j:
                row[i], row[j] = row[j]^1, row[i]^1

                i +=1
                j -=1
            
        return image 