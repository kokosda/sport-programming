class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        res = []
        sign = -1 if num < 0 else 1
        num = abs(num)
        
        while num > 0:
            m = num % 7
            res.append(m)
            num = num // 7
            
        if sign == -1:
            res.append('-')
            
        return ''.join([str(res[i]) for i in range(len(res) - 1, -1, -1)])