class Edge:
    def __init__(self, from_, to_, weight):
        self.from_ = from_
        self.to_ = to_
        self.weight = weight


def trace(x, path):
    if x == 0:
        return path
    else:
        return trace(pre[x], chr(pre[x] + 97) + '->' + path)


n, m = map(int, input().split())
edges = []
for _ in range(m):
    _from, _to, weight = input().split()
    weight = int(weight)
    edges.append(Edge(ord(_from) - 97, ord(_to) - 97, weight))
d = [0x3f3f3f3f] * n
pre = [i for i in range(n)]
d[0] = 0
for _ in range(n - 1):
    for edge in edges:
        if d[edge.from_] != 0x3f3f3f3f and d[edge.to_] >= d[edge.from_] + edge.weight:
            d[edge.to_] = d[edge.from_] + edge.weight
            pre[edge.to_] = edge.from_

if_negative = False
for edge in edges:
    if d[edge.from_] != 0x3f3f3f3f and d[edge.to_] > d[edge.from_] + edge.weight:
        if_negative = True

if if_negative:
    print('Negative-weight cycle found in the graph')
else:
    for i in range(1, n):
        if d[i] != 0x3f3f3f3f:
            print('{}: {}'.format(d[i], trace(i, chr(i + 97))))


"""
7 9
a b -1
b c 3
a c 4
b d 2
d b 1
b e 2
d c 5
e d -3
f g 2
"""

"""
5 8
a b -1
b c 3
a c 4
b d 2
d b 1
b e 1
d c 5
e d -3
"""