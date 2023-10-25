import numpy as np

A = np.array(list(map(int, input().split())))
n = len(A) - 1

dp = np.full((n, n), np.inf)
s = np.zeros((n, n), dtype=int)

for i in range(n):
    dp[i, i] = 0

for length in range(2, n + 1):  # 0, 1 i=0, j=0 + 2 - 1
    for i in range(0, n - length + 1):
        j = i + length - 1
        for k in range(i, j):
            if dp[i, k] + dp[k + 1, j] + A[i] * A[k + 1] * A[j + 1] < dp[i, j]:
                dp[i, j] = dp[i, k] + dp[k + 1, j] + A[i] * A[k + 1] * A[j + 1]
                s[i, j] = k

print(int(dp[0, n - 1]))


def search_solve(l, r):
    if l == r:
        return 'A{}'.format(l + 1)
    k = s[l, r]
    left = search_solve(l, k)
    right = search_solve(k + 1, r)
    return '({})'.format(left + right)


print(search_solve(0, n - 1))
