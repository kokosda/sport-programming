class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        i, j = 0, 0
        
        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                dp[i + 1] = dp[i]
                j += 1
            elif j + 1 < len(p) and p[j + 1] == "*" and p[j] != '.':
                j += 2
                continue                
            else:
                if p[j] == '.':
                    dp[i + 1] = dp[i]
                    j += 1
                elif p[j] == '*':
                    if p[j - 1] == '.':
                        dp[i + 1] = dp[i]
                        j += 1
                    else:
                        if s[i] == p[j - 1]:
                            dp[i + 1] = dp[i]
                            
                            if i + 1 < len(s) and s[i + 1] != p[j - 1]:
                                j += 1
            i += 1
        
        return dp[-1]
    
"""
dynamic state: [i, j] - prefixes in s and p
value func: string matches the pattern
initial state: dp[0][0] = true
transition funcs:
    1) s[i] == p[j]
    2) s[i+1] == p[j] if p[j] == '.'
    3) s[i+1] == p[j] if p[j] == '*' then s[i+1] == p[j-1]
order funcs: 0..|s|, 0..|p|
answer:

"aa"
"a"
"aa"
"a."
"aaa"
"a.a"
"aa"
"a*"
"ab"
".*"
"aab"
"c*a*b"
"mississippi"
"mis*is*p*."
"cab"
"c*."
""
""
"atq"
"a.q"
"aaatq"
"a*.q"
"aaatqqqf"
"a*.q*f"
"ab"
".*c"
"""