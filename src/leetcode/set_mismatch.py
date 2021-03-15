class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        store = [0] * (len(nums) + 1)
        res = []
        
        for i in nums:
            if store[i] is 0:
                store[i] += 1
            else:
                res.append(i)
                store[i] += 1
                
        for i in range(1, len(store)):
            if store[i] is 0:
                res.append(i)
                break
        
        return res