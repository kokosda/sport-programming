class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) <= 2:
            return sum(bits) is 0
        
        last_i = len(bits) - 1
        i = 0
        
        while i < last_i:
            if bits[i] is 1:
                i += 1
                
                if i == last_i:
                    return False                

            i += 1
        
        return True
    
"""
11 10 - 1,3,F
0 11 0 - 1,2,T
0 0 10 - 1,1,F
10 0 0 - 1,1,T

01110100
0111010
0101110
0100100
0101100
1101100
10 10 11 0 0 0
10 10 11 0 0 0
00
100110
100100
100010

00110
00100
00010

[1,0,0,0]
[0,0,1,0]
[1,0,0]
[1,1,1,0]
[1,0,0,0,1,1,0]
[0,0,0,0,0,0,0]
[0]
[1,0]
[1,0,1,1,1,0,0]
"""