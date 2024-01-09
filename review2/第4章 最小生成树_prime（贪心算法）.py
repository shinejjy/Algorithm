import heapq


def DecreaseKey(heap):
    new_heap = []
    while heap:
        heapq.heappush(new_heap, heapq.heappop(heap))
    return new_heap


class Dis:
    def __init__(self, idx):
        self.idx = idx
        self.dis = float('inf') if idx != 0 else 0
        self.adj = [v for v in range(n) if A[v][idx] != 0]

    def __lt__(self, other):
        return self.dis < other.dis


n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
pre = [i for i in range(n)]
V = [False] * n

dis_s = [Dis(i) for i in range(n)]
heap = []

for dis in dis_s:
    heapq.heappush(heap, dis)

while heap:
    dis_i = heapq.heappop(heap)
    V[dis_i.idx] = True
    if dis_i.idx != 0:
        print('{} {} {}'.format(dis_i.idx + 1, pre[dis_i.idx] + 1, A[pre[dis_i.idx]][dis_i.idx]))
    for v in dis_i.adj:
        if not V[v] and dis_s[v].dis > A[dis_i.idx][v]:
            pre[v] = dis_i.idx
            dis_s[v].dis = A[dis_i.idx][v]
            heap = DecreaseKey(heap)

"""
8
0 15 7 0 0 0 0 10
15 0 0 0 0 0 0 0
7 0 0 9 12 5 0 0 
0 0 9 0 0 0 0 0
0 0 12 0 0 6 0 0
0 0 5 0 6 0 14 8
0 0 0 0 0 14 0 3
10 0 0 0 0 8 3 0
"""
