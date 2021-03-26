class Solution:
    def rotatedDigits(self, N: int) -> int:
        mirror = [0,1,5,-1,-1,2,9,-1,8,6]
        res = 0
        
        for i in range(1, N + 1):
            mirrored = []
            
            for ch in str(i):
                r = mirror[int(ch)]
                
                if r is -1:
                    break
                
                mirrored.append(str(r))
            else:  
                mirrored = int(''.join(mirrored))
                
                if mirrored != i:
                    res += 1
                
        return res