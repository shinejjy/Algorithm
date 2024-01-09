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
"""
0: A[0, 1]
1: A[1, 2]
dp[0][0] = 0
dp[0][1] = dp[0][0] * dp[0][1]
"""
