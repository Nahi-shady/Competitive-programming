class DataStream:

    def __init__(self, value: int, k: int):
        self.de = deque()
        self.value = value
        self.k = k
        self.length = 0
        self.wrong = 0

    def consec(self, num: int) -> bool:
        self.de.append(num)
        if num != self.value:
            self.wrong += 1
        self.length += 1
        if self.length < self.k:
            return
        if self.wrong == 0:
            self.de.popleft()
            self.length -= 1
            return True
        if self.de[0] != self.value:
            self.wrong -= 1
        self.de.popleft()
        self.length -= 1
        return 



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)