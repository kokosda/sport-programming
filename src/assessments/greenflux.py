from typing import List

class Suggestion:
    def __init__(self, a: List[int]):
        self.list = a[:]

    def add(self, idx: int):
        self.list.append(idx)

    def __str__(self) -> str:
        return f'Suggestion({str(self.list)})'

    def __repr__(self) -> str:
        return f'Suggestion({str(self.list)})'

class Solution:
    def get_suggestions(capacity: int, connectors: List[int], current_new: int) -> List[Suggestion]:
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
                suggestion = Suggestion([pos])

                while freeing_cap_tmp > 0 and len(suggestion.list) < last_suggestions_count:
                    pos = Solution.bisect_left(connectors, freeing_cap_tmp, pos)

                    if pos < len(connectors) and (freeing_cap_tmp - connectors[pos] >= 0):
                        suggestion.add(pos)
                        freeing_cap_tmp -= connectors[pos]
                    else:
                        break

                if freeing_cap_tmp is 0 and len(suggestion.list) <= last_suggestions_count:
                    last_suggestions_count = len(suggestion.list)
                    res.append(suggestion)

            i += 1

        res = [s for s in res if len(s.list) == last_suggestions_count]
        res = res + Solution.get_indices_combinations(res, connectors)

        return res

    def get_indices_combinations(suggestions: List[Suggestion], connectors: List[int]) -> List[Suggestion]:
        res = []

        for suggestion in suggestions:
            for suggestion_list_idx in range(len(suggestion.list)):
                index_in_connectors = suggestion.list[suggestion_list_idx]
                next_connector_idx = len(connectors)

                if suggestion_list_idx + 1 < len(suggestion.list):
                    next_connector_idx = suggestion.list[suggestion_list_idx + 1]

                i = index_in_connectors + 1

                while i < next_connector_idx and connectors[i] == connectors[index_in_connectors]:
                    s = Suggestion(suggestion.list) #fix error of impossible Suggestion like [4,4,5] produced from [3,4,5] (connectors: [16,9, 7, 5, 5, 3, 3, 2, 2, 1, 1])
                    s.list[suggestion_list_idx] = i
                    res.append(s)
                    i += 1

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

capacity = 56
connectors = [16,9, 7, 5, 5, 3, 3, 2, 2, 1, 1]
current_new = 15
suggestions = Solution.get_suggestions(capacity, connectors, current_new)
print([",".join([str(connectors[i]) for i in s.list]) for s in suggestions])
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

[Suggestion([1, 5, 9]), Suggestion([2, 3, 9]), Suggestion([3, 4, 5]), Suggestion([1, 6, 9]), Suggestion([1, 5, 10]), Suggestion([2, 4, 9]), Suggestion([2, 3, 10]), Suggestion([4, 4, 5]), Suggestion([3, 4, 6])]
[Suggestion([1, 5, 9]), Suggestion([2, 3, 9]), Suggestion([3, 4, 5]), Suggestion([1, 6, 9]), Suggestion([1, 5, 10]), Suggestion([2, 4, 9]), Suggestion([2, 3, 10]), Suggestion([3, 4, 6])]
"""