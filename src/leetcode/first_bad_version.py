# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        
        s = 1
        e = n + 1
        mem = {}
        mem[s] = isBadVersion(s)
        
        if mem[s]:
            return s
        
        while True:
            m = (e + s) // 2
            mem[m] = isBadVersion(m)
            
            if mem[m]:
                e = m
            else:
                s = m
                
            if s + 1 == e and not mem[s] and mem[e]:
                break
                
        return e
    
"""
n = 2
bad = 2

s, e = 1, 2
mem[{1: True}]

n = 3
bad = 3

s, e = 2, 3
mem[{1: False},{2: False},{3: True}]
m = 3

"""