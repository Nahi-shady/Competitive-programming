class RecentCounter:

    def __init__(self):
        self.de = deque()
        self.length = 0
    def ping(self, t: int) -> int:
        self.de.append(t)
        self.length += 1
        while self.de and self.de[0] < t-3000:
            self.de.popleft()
            self.length -= 1
        return self.length
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)