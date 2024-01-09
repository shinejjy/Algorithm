import heapq

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]


class Node:
    def __init__(self, idx, A, d=0x3f3f3f3f):
        self.idx = idx
        self.d = d
        self.adj = [(j, A[self.idx][j]) for j in range(n) if A[self.idx][j] > 0]

    def __lt__(self, other):
        return self.d < other.d


def print_path(pre, idx):
    if pre[idx] == idx:
        return ''
    else:
        return print_path(pre, pre[idx]) + '{}->'.format(pre[idx] + 1)


pre = [i if A[0][i] == 0 else 0 for i in range(n)]
nodes = [Node(i, A, 0) if i == 0 else Node(i, A, 0x3f3f3f3f if A[0][i] == 0 else A[0][i]) for i in range(n)]
heap = []
for i in range(1, n):
    heapq.heappush(heap, nodes[i])

while heap:
    node = heapq.heappop(heap)
    for idx, dis in node.adj:
        if node.d + dis < nodes[idx].d:
            nodes[idx].d = node.d + dis
            pre[idx] = node.idx

for i in range(1, n):
    print('{}: {}{}'.format(nodes[i].d, print_path(pre, i), i + 1) if pre[i] != i else 'inf: 1->{}'.format(i + 1))

"""
5
0 10 0 30 100
0 0 50 0 0
0 0 0 0 10
0 0 20 0 60
0 0 0 0 0
"""
