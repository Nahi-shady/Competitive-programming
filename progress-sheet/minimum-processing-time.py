class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        n = 3
        tot = 0
        for num in processorTime:
            tot = max(tasks[n] + num, tot)
            n += 4

        return tot