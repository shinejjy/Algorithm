import numpy as np
from queue import LifoQueue

m, n = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(m)]

dp = np.full((m + 1, n + 1), float('inf'))

dp[0, 1] = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[i, j] = mat[i - 1][j - 1] + min(dp[i - 1, j], dp[i, j - 1])


i, j = m, n
q = LifoQueue()
q.put([i, j])
while i != 1 or j != 1:
    if dp[i - 1, j] > dp[i, j - 1]:
        j -= 1
    else:
        i -= 1
    q.put([i, j])

print(int(dp[m, n]))

while not q.empty():
    print(' '.join(map(str, q.get())))

"""
4 4
1 3 5 9
8 1 3 4
5 0 6 1
8 8 4 0
"""