class HitCounter:

    def __init__(self):
        self.hitTimes = {}
        self.hits = 0
        self.last_hit = 0

    def hit(self, timestamp: int) -> None:
        self.hitTimes[timestamp] = self.hits
        self.hits += 1
        self.last_hit = timestamp

    def getHits(self, timestamp: int) -> int:
        result = []
        mx = 0
        for hit in self.hitTimes:
            if timestamp - hit < 3000:            
                mx += 1
        return mx


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)