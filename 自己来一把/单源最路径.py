import heapq


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.dis = float('inf') if idx != 0 else 0
        self.adj = [i for i in range(n) if A[idx][i] > 0]

    def __lt__(self, other):
        return self.dis < other.dis


def DecreaseKey(heap):
    new_heap = []
    while heap:
        heapq.heappush(new_heap, heapq.heappop(heap))
    return new_heap


n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
pre = [i for i in range(n)]
nodes = [Node(i) for i in range(n)]
heap = []
for node in nodes:
    heapq.heappush(heap, node)

while heap:
    node = heapq.heappop(heap)
    for idx in node.adj:
        if nodes[idx].dis > node.dis + A[node.idx][idx]:
            nodes[idx].dis = node.dis + A[node.idx][idx]
            pre[idx] = node.idx
            heap = DecreaseKey(heap)


def search(idx):
    if pre[idx] == idx:
        return ''
    return search(pre[idx]) + '{}->'.format(pre[idx] + 1)


for i in range(1, n):
    if pre[i] != i:
        print('{}: {}{}'.format(nodes[i].dis, search(i), i + 1))
    else:
        print('inf: 1->{}'.format(i+1))
