# 矩阵连乘
import numpy as np

A = list(map(int, input().split()))
n = len(A) - 1
dp = [[float('inf') for _ in range(n)] for _ in range(n)]
p = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 0
for step in range(1, n):
    for i in range(n - step):
        j = i + step
        for k in range(i, j):
            if dp[i][j] > dp[i][k] + dp[k + 1][j] + A[i] * A[k + 1] * A[j + 1]:
                dp[i][j] = dp[i][k] + dp[k + 1][j] + A[i] * A[k + 1] * A[j + 1]
                p[i][j] = k

print(np.array(dp))
print(np.array(p))


def search(i, j):
    if i == j:
        return 'A{}'.format(i + 1)
    left = search(i, p[i][j])
    right = search(p[i][j] + 1, j)
    return '({})'.format(left + right)


print(search(0, n - 1))

# 最长公共子序列
import copy

X = input().split()
Y = input().split()


def search(i, j, state):
    if i == 0 or j == 0:
        print(state)
        return
    new_state = copy.deepcopy(state)
    if p[i][j] == 0:
        new_state = X[i - 1] + new_state
        search(i - 1, j - 1, new_state)
    elif p[i][j] == 1:
        search(i, j - 1, new_state)
    elif p[i][j] == 2:
        search(i - 1, j, new_state)
    else:
        search(i, j - 1, new_state)
        search(i - 1, j, new_state)


dp = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]
p = [[-1 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]
for i in range(1, len(X) + 1):
    for j in range(1, len(Y) + 1):
        if X[i - 1] == Y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            p[i][j] = 0
        elif dp[i][j - 1] > dp[i - 1][j]:
            dp[i][j] = dp[i][j - 1]
            p[i][j] = 1
        elif dp[i][j - 1] < dp[i - 1][j]:
            dp[i][j] = dp[i - 1][j]
            p[i][j] = 2
        else:
            dp[i][j] = dp[i - 1][j]
            p[i][j] = 3

print(dp[-1][-1])
if dp[-1][-1] == 0:
    print(None)
else:
    search(len(X), len(Y), '')


# 最小生成树prime
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

# 最大子段和
a = list(map(int, input().split()))
b = 0
best = -float('inf')
best_l = best_r = 0

l = r = 0
for i in range(len(a)):
    r = i
    if b > 0:
        b += a[i]
    else:
        l = i
        b = a[i]

    if b > best:
        best = b
        best_l = l
        best_r = r

print(best)
print(best_l + 1)
print(best_r + 1)

# 哈夫曼
import heapq
import math


class Node:
    def __init__(self, fr, nodes=[]):
        self.fr = fr
        self.code = ''
        self.nodes = nodes

    def __lt__(self, other):
        return self.fr < other.fr


n = int(input())
frs = list(map(int, input().split()))
init_node = [Node(fr) for fr in frs]
nodes = [Node(frs[i], [init_node[i]]) for i in range(n)]
heap = []
for node in nodes:
    heapq.heappush(heap, node)
while len(heap) > 1:
    left = heapq.heappop(heap)
    for node in left.nodes:
        node.code = '0' + node.code
    right = heapq.heappop(heap)
    for node in right.nodes:
        node.code = '1' + node.code
    new_code = Node(left.fr + right.fr, left.nodes + right.nodes)
    heapq.heappush(heap, new_code)

for i in range(n):
    print('{} {}'.format(chr(i + 97), init_node[i].code))

compressed = sum([len(init_node[i].code) for i in range(n)])
ori = n * math.ceil(math.log2(n))
print(ori / compressed)


# 单源最短路
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

# 多边形
import math

import numpy as np

n = int(input())
pts = [list(map(int, input().split())) for _ in range(n)]
dis = [[(lambda i, j: math.sqrt((pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2))(i, j) for i in range(n)]
       for j in range(n)]

dp = [[float('inf') for _ in range(n)] for _ in range(n)]
p = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n - 1):
    dp[i][i + 1] = dis[i][i + 1]

for step in range(2, n):
    for i in range(n - step):
        j = i + step
        for k in range(i + 1, j):
            if dp[i][k] + dp[k][j] + dis[i][j] < dp[i][j]:
                dp[i][j] = dp[i][k] + dp[k][j] + dis[i][j]
                p[i][j] = k

print(np.array(p))


def search(i, j):
    if i + 1 == j:
        return
    k = p[i][j]
    search(i, k)
    search(k, j)
    print("{}{}{}".format(i, k, j))


search(0, n - 1)


# 背包
import copy

init = lambda height, width, value: [[value for _ in range(width)] for _ in range(height)]

c = int(input())
n = int(input())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

dp = init(n + 1, c + 1, 0)

for i in range(min(c, w[-1]), c + 1):
    dp[n][i] = v[-1]

for i in range(n - 1, 0, -1):
    for j in range(1, c + 1):
        if j < w[i - 1]:
            dp[i][j] = dp[i + 1][j]
        else:
            if dp[i + 1][j] > dp[i + 1][j - w[i - 1]] + v[i - 1]:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j - w[i - 1]] + v[i - 1]

print(dp[1][c])


def search(i, j, state):
    new_state = copy.deepcopy(state)
    if i == n:
        if j >= w[-1]:
            new_state.append(i)
        print(new_state)
        return
    if dp[i][j] != dp[i + 1][j]:
        new_state.append(i)
        search(i + 1, j - w[i - 1], new_state)
    else:
        if dp[i + 1][j] == dp[i + 1][j - w[i - 1]] + v[i - 1]:
            new_state.append(i)
            search(i + 1, j - w[i - 1], new_state)
        else:
            search(i + 1, j, new_state)


search(1, c, [])

