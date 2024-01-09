import math
import numpy as np


def compute_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]
dis = np.array([[compute_distance(pos[i], pos[j]) for j in range(n)] for i in range(n)], dtype=int)
dp = np.zeros((n, n), dtype=int)
p = np.zeros((n, n), dtype=int)

for i in range(n - 1):
    dp[i, i + 1] = dis[i, i + 1]

for step in range(2, n):
    for i in range(0, n - step):
        j = i + step
        for k in range(i + 1, j):
            if dp[i, j] == 0 or dp[i, j] > dp[i, k] + dp[k, j] + dis[i, j]:
                dp[i, j] = dp[i, k] + dp[k, j] + dis[i, j]
                p[i, j] = k


def search_and_print_best(p, i, j):
    if j - 1 == i:
        return
    k = p[i, j]
    search_and_print_best(p, i, k)
    search_and_print_best(p, k, j)
    print("{}{}{}".format(i, k, j))


search_and_print_best(p, 0, n - 1)


"""
7
8 26
0 20
0 10
10 0
22 12
27 21
15 26
"""

"""
假设N个点，其实我们最后要求的是weight[0, N - 1]
1. 计算各个点对的距离，即d[i, j]
2. 初始化weight矩阵
    weight[i, i] = 0
    weight[i, i + 1] = d[i, i + 1]
3. 线性DP，遍历间隔
    for 间隔 = 2 to N - 1 （间隔=1的时候已经有了）
        for i = 0 to N - 间隔 - 1
            j = i + 间隔
            for s = i + 1 to j - 1 （遍历分割点）
            weight[i, j] = min(weight[i, j], weight[i, k] + weight[k, j] + d[i, j])
"""