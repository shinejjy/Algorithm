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
