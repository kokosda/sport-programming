class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        
        i = 0
        j = 0
        prev_i = 0
        
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                prev_i = i
                i += 1
                j += 1
            else:
                prev_j = j
                
                while j < len(typed) and name[prev_i] == typed[j]:
                    j += 1
                else:
                    if prev_j is j or (j < len(typed) and name[i] != typed[j]):
                        return False
                    
        while j < len(typed):
            if typed[j] != name[-1]:
                return False
            j += 1
            
        return i == len(name) and j == len(typed)
"""
n:aalex
      ^
t:aaaleexxyz
        ^
     
saeed
   ^
ssaaedd
     ^

"pyplrz"
      ^
"ppyypllr"
         ^

cn: 1
ct: 2

"pyplrz"
"ppyypllr"
"rick"
"kric"
"alex"
"aaleex"
"saeed"
"ssaaedd"
"leelee"
"lleeelee"
"t"
"m"
"tt"
"t"
"tt"
"ttt"
"tt"
"tt"

вспомнить, что сделали в i_odd, i_even (просто взяли 2 указатели и двигали когда пора и смотрели на их состояние)
"""