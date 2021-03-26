class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        nums = self.nums
        
        if len(nums) < self.k:
            heapq.heappush(nums, val)
        else:
            heapq.heappushpop(nums, val)
            
        return nums[0]

class KthLargestArray:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._nums = sorted(nums)[-k:]
        self._k_pos = 0

    def add(self, val: int) -> int:
        i = bisect.bisect_left(self._nums, val)
        
        if len(self._nums) < self._k:
            self._nums = (self._nums[:i] + [val] + self._nums[i:])[-self._k:]
            return self._nums[0]

        if i > 0:
            if self._nums[-1] <= val:
                self._nums.append(val)
                self._k_pos += 1
            else:
                self._nums = (self._nums[:i] + [val] + self._nums[i:])[-self._k:]
                self._k_pos = 0
                
        return self._nums[self._k_pos]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
["KthLargest","add","add","add","add","add"]
[[2,[0]],[-1],[1],[-2],[-4],[3]]
["KthLargest","add","add","add","add","add"]
[[1,[]],[-3],[-2],[-4],[0],[4]]
["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
"""