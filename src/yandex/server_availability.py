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

class RequestStats:
    def __init__(self, timestamp: int) -> None:
        self.requests = deque(Request(timestamp, 1))
        self.total_count = 1

def collapse_queue(q: Deque[Request], timestamp: int, duration: int) -> int:
    if len(q) is 0:
        return

    diff = 0

    if q[-1].time + duration < timestamp:
        q.clear()
        return

    while len(q) is not 0 and q[0].time + duration < timestamp:
        request = q.popleft()
        diff = request.count - diff

        if len(q) is not 0:
            q[-1].count -= diff

def is_request_allowed(q: Deque[Request], limit: int) -> bool:
    if len(q) is not 0 and q[-1].count == limit:
        return False

    return True

def add_request(q: Deque[Request], timestamp: int) -> None:
    if len(q) is 0:
        q.append(Request(timestamp, 1))
        return

    if q[-1].time == timestamp:
        q[-1].count += 1
    else: 
        q.append(Request(timestamp, q[-1].count + 1))

fin = open('input.txt')
user_limit, service_limit, duration = map(int, fin.readline().split())
s = [None]
requests_by_users = {}
requests_by_service = deque()

while True:
    s = fin.readline().split()

    if s[0] == '-1':
        break

    timestamp, user_id = map(int, s)

    collapse_queue(requests_by_service, timestamp, duration)

    if requests_by_users.get(user_id) is not None:
        if not is_request_allowed(requests_by_users[user_id], user_limit):
            print(timestamp, 400, requests_by_service, requests_by_users)

    if not is_request_allowed(requests_by_service, service_limit):
        print(timestamp, 500, requests_by_service, requests_by_users)
        continue

    if requests_by_users.get(user_id) is None:
        requests_by_users[user_id] = deque()

    user_q = requests_by_users[user_id]

    collapse_queue(user_q, timestamp, duration)

    if not is_request_allowed(user_q, user_limit):
        print(timestamp, 400, requests_by_service, requests_by_users)
        continue

    add_request(user_q, timestamp)
    add_request(requests_by_service, timestamp)
    print(timestamp, 200, requests_by_service, requests_by_users)

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
[[2,4]]
[[3,5]]
[[8,4]]
"""