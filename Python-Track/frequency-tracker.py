class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freq2 = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[number] += 1
        self.freq2[self.freq[number]] += 1

        if self.freq2[self.freq[number]-1] > 0:
            self.freq2[self.freq[number]-1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number] > 0:
            self.freq[number] -= 1
            if self.freq2[self.freq[number]+1] > 0:
                self.freq2[self.freq[number]+1] -= 1
            
            self.freq2[self.freq[number]] += 1


    def hasFrequency(self, frequency: int) -> bool:
        if self.freq2[frequency]:
            return True


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)