from typing import List

class Solution:
    def get_suggestions(capacity: int, connectors: List[int], current_new: int) -> List[List[int]]:
        if current_new > capacity:
            return []
        
        connectors = sorted(connectors, reverse=True)
        available_cap = capacity - sum(connectors)

        if available_cap >= current_new:
            return []

        res = []
        FREEING_CAP = current_new - available_cap
        last_suggestions_count = len(connectors)
        i = 0

        while i < len(connectors):
            if connectors[i] <= current_new:
                pos = i
                freeing_cap_tmp = FREEING_CAP - connectors[pos]
                suggestion = [pos]

                while freeing_cap_tmp > 0 and len(suggestion) < last_suggestions_count:
                    pos = Solution.bisect_left(connectors, freeing_cap_tmp, pos)

                    if pos < len(connectors) and (freeing_cap_tmp - connectors[pos] >= 0):
                        suggestion.append(pos)
                        freeing_cap_tmp -= connectors[pos]
                    else:
                        break

                if freeing_cap_tmp is 0 and len(suggestion) <= last_suggestions_count:
                    last_suggestions_count = len(suggestion)
                    res.append(suggestion)

            i += 1

        res = [s for s in res if len(s) == last_suggestions_count]
        return res

    def bisect_left(arr: List[int], val: int, lo: int):
        l = lo
        r = len(arr)

        while r - l > 1:
            e = (l + r) >> 1

            if arr[e] > val: 
                l = e
            else: 
                r = e

        return r

capacity = 40
connectors = [9, 7, 6, 5, 3, 3, 2, 2, 1]
current_new = 15
suggestions = Solution.get_suggestions(capacity, connectors, current_new)
print(suggestions)

"""
cap: 40
connectors: [9, 7, 5, 5, 3, 3, 2, 2, 1, 1]
current_new: 15
----
available_cap = 40 - 38 = 2
FREEING_CAP: 15 - 2 = 13
last_suggestions_count: 9
pos: 0
freeing_cap_tmp: 13
suggestion: [0,4,8]
res: []
"""