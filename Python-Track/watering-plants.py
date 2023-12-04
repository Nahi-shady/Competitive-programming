class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        cap = capacity
        for i in range(len(plants)):
            if plants[i] <= cap:
                cap -= plants[i]
            else:
                steps += i*2
                cap = capacity - plants[i]
            steps += 1
        return steps