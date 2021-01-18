import heapq

class Event:
    def __init__(self, start_day: int, end_day: int):
        self.start_day = start_day
        self.end_day = end_day

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        sorted_events = [Event(e[0], e[1]) for e in sorted(events)]        
        total_days = max([e.end_day for e in sorted_events])
        min_heap = []
        day, event_index, count = 1, 0, 0

        while day <= total_days:
            if event_index < len(sorted_events) and not min_heap:
                day = sorted_events[event_index].start_day

            while event_index < len(sorted_events) and sorted_events[event_index].start_day <= day:
                heapq.heappush(min_heap, sorted_events[event_index].end_day)
                event_index += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                count += 1
            elif event_index >= len(sorted_events):
                break

            day += 1

        return count

"""
[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
[[1,100000]]
[[1,2],[1,7],[3,4],[3,6],[3,3],[4,5],[4,6]]
[[1,2],[5,8],[3,6],[9,10],[10,12],[12,15],[14,15]]
[[1,2],[2,3],[3,4]]
"""
