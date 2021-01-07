class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda el: el[0])
        start, end, last = 0, 1, -1
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            print(cur_interval)
            if cur_interval[start] <= result[last][end] and cur_interval[end] >= cur_interval[start]:
                result[last][start] = min(result[last][start], cur_interval[start])
                result[last][end] = max(result[last][end], cur_interval[end])
            else:
                result.append(cur_interval)
        return result
