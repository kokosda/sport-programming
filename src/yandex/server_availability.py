fin = open('input.txt')
user_limit, service_limit, duration = map(int, fin.readline().split())
s = fin.readline().split()

while s[0] != '-1':
    user_id, timestamp = map(int, s)
    s = fin.readline().split()

fin.close()

"""
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
"""