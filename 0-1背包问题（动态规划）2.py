import numpy as np


def search_ans(dp, c, i):
    if i == n - 1:
        if c >= w[i]:
            print(i + 1, end=' ')
        return
    if dp[i][c] == dp[i + 1][c]:
        search_ans(dp, c, i + 1)
    else:
        print(i + 1, end=' ')
        search_ans(dp, c - w[i], i + 1)


c = int(input())
n = int(input())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    for j in range(1, c + 1):
        if j < w[i]:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])

print(dp[0][c])
search_ans(dp, c, 0)


"""
10
5
6 3 5 4 6
2 2 6 5 4
"""
