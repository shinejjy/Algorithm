import heapq


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.dis = float('inf') if idx != 0 else 0
        self.adj = [i for i in range(n) if A[i][idx] > 0]
        self.visit = False

    def __lt__(self, other):
        return self.dis < other.dis


def DecreaseKey(heap):
    new_heap = []
    while heap:
        heapq.heappush(new_heap, heapq.heappop(heap))
    return new_heap


n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

nodes = [Node(i) for i in range(n)]
pre = [i for i in range(n)]

heap = []
for node in nodes:
    heapq.heappush(heap, node)

while heap:
    node = heapq.heappop(heap)
    node.visit = True
    if node.idx != 0:
        print('{} {} {}'.format(node.idx + 1, pre[node.idx] + 1, A[node.idx][pre[node.idx]]))
    for adj_idx in node.adj:
        if nodes[adj_idx].dis > A[adj_idx][node.idx] and not nodes[adj_idx].visit:
            nodes[adj_idx].dis = A[adj_idx][node.idx]
            pre[adj_idx] = node.idx
            heap = DecreaseKey(heap)
