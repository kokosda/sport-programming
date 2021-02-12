class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values = set()
        
        for i in nums:
            if i not in values:
                values.add(i)
            else:
                return True
            
        return False

"""
[1,2,3]
[3,3]
[1]
[11,11,11]
"""