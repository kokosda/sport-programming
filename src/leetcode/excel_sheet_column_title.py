class Solution:
    def convertToTitle(self, n: int) -> str:        
        basis = 26
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        
        while n > 0:
            i = (n - 1) % basis
            result += chars[i]
            n = (n - 1) // basis
            
        return result[::-1]
        
"""
701 = 1*26*26 + 0*26 + 25*26^0 - ZY
701 = 1*25*26 + 1*26 + 25*26^0 - ZY
700 = 1*26*26 + 0*26 + 24*26^0 - ZX

AA - 27
AB - 28
...
AY - 51
AZ - 52
BA - 53
BB - 54
...
BZ - 78
CA - 79

6 // 2: 3(0)
3 // 2: 1(1)
1 // 2: 0(1)
110

28 // 26: 1(2)
1  // 26: 0(1)

28-1 // 26: 1(1)
1-1 // 26: 0(0)

700-1 // 26: 26(24) - Y
26-1 // 26: 0(25) - Z
"""