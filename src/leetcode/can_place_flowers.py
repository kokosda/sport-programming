class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            return flowerbed[0] == 1 and n == 0
        
        if flowerbed[0] == 0 and flowerbed[1] == 0 and n > 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0 and n > 0:
            flowerbed[-1] = 1
            n -= 1
        
        if n > 0:
            i = 1
            
            while n > 0 and i < (len(flowerbed) - 1):
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    
                i += 1

        res = (n == 0)
        return res
    
"""
[0]
1
[0]
0
[1]
0
[1]
1
[0,0,0,0]
3
[1,0,0,0,1]
1
"""