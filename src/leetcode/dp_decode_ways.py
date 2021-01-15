class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        dp = [1] * (len(s) + 2)
        i = len(s) - 1

        while i > 0:
            pair = [s[i - 1], s[i]]

            if (pair[0] == '0' or pair[0] > '2') and pair[1] == '0':
                return 0

            if i + 1 >= len(s) or s[i + 1] > '0':
                if pair[0] == '1' and pair[1] != '0':
                    dp[i] = dp[i + 1] + dp[i + 2]
                elif pair[0] == '2' and pair[1] > '0' and pair[1] <= '6':
                    dp[i] = dp[i + 1] + dp[i + 2]

            dp[i] = max(dp[i + 1], dp[i])    
            i -= 1

        return dp[1]
    
"""
dynamic state: letter A-Z
dynamic value: number of ways
initial state: dp[n]
transition:
    1) 0 - only 10, 20; impossible if self only
    2) pair [i,j] - if i > 2 then only 1 option: 2 letters
    3) pair [i,j] - if i > 0 and i <= 2 then 2 options possible: A/B [1/2] and [0-9] or [10-26]
order funcs: 0..n
answer: dp[0]

A-1
...
L-12
...
Z-26
12

"1720101" - 17, 20, 10, 1
"1720101" - 1, 7, 20, 10, 1

01[] - 1 - impossible
10[1] - 1
01[01] - 1 - impossible
20[101] - 1
72[0101] - 1 - impossible
17[20101] - 2 [1,7 or 17]

1111[1] - 1
111[11] - 2
11[11]1 - 3 (2+1)
1[11]11 - 5 (3+2)
[11]111 - 8 (5+3)


"2010"
"01"
"00"
"10"
"30"
"2003"
"1720101"
"226"
"2101"


"""