class RecentCounter:
    LIMIT = 3000
    
    def __init__(self):
        self.nums = deque()
        
    def ping(self, t: int) -> int:
        self.nums.append(t)

        if len(self.nums) > 1:
            idx = bisect.bisect_left(self.nums, t - RecentCounter.LIMIT)
            i = 0
            
            while i < idx:
                self.nums.popleft()
                i += 1
        
        return len(self.nums)

    def ping_heap(self, t: int) -> int:
        if len(self.nums) is 0:
            self.nums.append(t)
        else:            
            while len(self.nums) > 0 and self.nums[0] < t - RecentCounter.LIMIT:
                heapq.heappop(self.nums)
            else:
                heapq.heappush(self.nums, t)
                
        return len(self.nums)
        
"""
10, 100, 200, 3100
1,  2,   3    2

pt = 198,199,200 (3)
t = 4000 (1000)
["RecentCounter","ping","ping","ping","ping"]
[[],[1],[100],[3001],[3002]]
["RecentCounter","ping","ping","ping","ping","ping"]
[[],[642],[1849],[4921],[5936],[5957]]
"""

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)