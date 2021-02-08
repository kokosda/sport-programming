class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_n = len(numbers)
        
        for i in range(len_n):
            d = target - numbers[i]
            k = bisect.bisect_left(numbers, d, i + 1, -1)
            
            if k != len_n and numbers[k] == d:
                return [i + 1, k + 1]
            
        return None
    
"""
[-2,1,5,6,8], t = 7
"""