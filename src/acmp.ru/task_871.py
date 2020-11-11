import queue

def is_cycled_graph(graph):
    q = queue.Queue()
    q.put(1)
    used = { 1: True }
    parents = { 1: -1 }
    is_cycled = False

    while (q.qsize() > 0):
        vertice = q.get()

        for i in graph[vertice]:
            to = i

            if used.get(to) == None:
                used[to] = True
                q.put(to)
                parents[to] = vertice
            elif parents.get(vertice) != to:
                is_cycled = True
                break

    return is_cycled

fin  = open("input.txt")

n, m = map(int, fin.readline().split())
graph = {}

for i in range(1, n + 1):
    graph[i] = set()

for i in range(m):
    pair = list(map(int, fin.readline().split()))
    graph[pair[0]].add(pair[1])

if is_cycled_graph(graph):
    print('YES')
else:
    print('NO')

fin.close()