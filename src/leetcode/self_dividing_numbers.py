class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for d in range(left, right + 1):
            t = d
            
            while t > 0:
                rem = t % 10
                t //= 10
                
                if rem is 0 or d % rem is not 0:
                    break
            else:
                res.append(d)
                
        return res