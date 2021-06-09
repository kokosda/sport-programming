from collections import deque
from typing import Deque, Tuple

class Request:
    def __init__(self, time: int, count: int) -> None:
        self.time = time
        self.count = count

    def __str__(self) -> str:
        return f'Request(t={self.time}, count={self.count})'

    def __repr__(self) -> str:
        return f'Request(t={self.time}, count={self.count})'

class Stats:
    def __init__(self) -> None:
        self.requests = deque()
        self.total_count = 0

    def __repr__(self) -> str:
        return f'Stats(tc: {self.total_count}, r:{self.requests}'

def collapse_queue(stats: Stats, timestamp: int, duration: int) -> int:
    if len(stats.requests) is 0:
        return

    if stats.requests[-1].time + duration < timestamp:
        stats.requests.clear()
        return

    while len(stats.requests) is not 0 and stats.requests[0].time + duration < timestamp:
        request = stats.requests.popleft()
        stats.total_count -= request.count

def is_request_allowed(stats: Stats, limit: int) -> bool:
    if len(stats.requests) is not 0 and stats.total_count == limit:
        return False

    return True

def add_request(stats: Stats, timestamp: int) -> None:
    stats.total_count += 1

    if len(stats.requests) > 0 and stats.requests[-1].time == timestamp:
        stats.requests[-1].count += 1
    else:
        stats.requests.append(Request(timestamp, 1))

fin = open('input.txt')
user_limit, service_limit, duration = map(int, fin.readline().split())
s = [None]
users_stats_map = {}
service_stats = Stats()

while True:
    s = fin.readline().split()

    if s[0] == '-1':
        break

    timestamp, user_id = map(int, s)

    collapse_queue(service_stats, timestamp, duration)

    if users_stats_map.get(user_id) is not None:
        if not is_request_allowed(users_stats_map[user_id], user_limit):
            print(timestamp, 400, service_stats, users_stats_map)
            continue

    if not is_request_allowed(service_stats, service_limit):
        print(timestamp, 500, service_stats, users_stats_map)
        continue

    if users_stats_map.get(user_id) is None:
        users_stats_map[user_id] = Stats()

    user_stats = users_stats_map[user_id]

    collapse_queue(user_stats, timestamp, duration)

    if not is_request_allowed(user_stats, user_limit):
        print(timestamp, 400, service_stats, users_stats_map)
        continue

    add_request(user_stats, timestamp)
    add_request(service_stats, timestamp)
    print(timestamp, 200, service_stats, users_stats_map)

fin.close()

"""
мы храним запросы на пользователя в словаре: 
    <user_id>: queue[(time, requests_count)]
также нужен счётчик сервисных запросов за последние n сек.

2(userlim) 5(serv) 5(dur)
time, user_id
1 100 -- 200
1 100 -- 200
2 100 -- 400
2 200 -- 200
2 300 -- 200
2 400 -- 200
2 500 -- 500
3 500 -- 500
5 200 -- 500
6 100 -- 400
7 100 -- 200
7 200 -- 200

1: 2
sl: 5

users:
{
    100: {
        (1,1,2,6)
        1: ok, ok
        2: err1
        6: err1
    },
    200: {
        2: ok
        5: err2,
        7: ok
    }
    300: {
        2: ok
    }
    400: {
        2: ok
    }
    500: {
        2: err2
        3: err2
    }
}
user_limit = 5, duration = 5

[[1,3]]
[[2,1]]
[[3,1]]
"""