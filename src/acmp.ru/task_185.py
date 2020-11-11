import queue

def get_graph(edges, size):
    graph = {}

    for i in range(1, size + 1):
        graph[i] = []

    for edge in edges:
        v1, v2 = edge[0], edge[1]
        graph[v1].append(v2)

    return graph

def traverse_graph(graph, k):
    q = queue.Queue()
    q.put(k)
    used = { k: True }
    parents = { k: -1 }

    while (q.qsize() > 0):
        vertice = q.get()

        for i in graph[vertice]:
            to = i

            if used.get(to) == None:
                used[to] = True
                q.put(to)
                parents[to] = vertice

    return { "parents": parents, "used": used }

fin  = open("input.txt")

n, k = map(int, fin.readline().split())
edges = []

pair = list(map(int, fin.readline().split()))

while len(pair) == 2:
    edges.append(pair)
    pair = list(map(int, fin.readline().split()))

graph = get_graph(edges, n)
traverse_info = traverse_graph(graph, k)

if len(traverse_info['used']) == n:
    print('Yes')
else:
    print('No')

fin.close()