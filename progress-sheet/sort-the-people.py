class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            min_idx = i
            for j in range(i+1, len(names)):
                if heights[j] > heights[min_idx]:
                    min_idx = j

            heights[i], heights[min_idx] = heights[min_idx], heights[i]
            names[i], names[min_idx] = names[min_idx], names[i]

        return names