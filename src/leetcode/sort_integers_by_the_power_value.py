class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = []
        
        for i in range(lo, hi + 1):
            x = i
            p = 0
            
            while x != 1:
                if x % 2 is 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                p += 1
                
            heapq.heappush(nums, (p, i))
            
        res = 0
        
        while k > 0:
            res = heapq.heappop(nums)[1]
            k -= 1
            
        return res
            
                    