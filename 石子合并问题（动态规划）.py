n = int(input())
a = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]
p = [[0 for _ in range(n)] for _ in range(n)]


for step in range(1, n):
    for i in range(0, n - step):
        j = i + step
        for k in range(i + 1, j + 1):
            s = 0
            for o in range(i, j + 1):
                s += a[o]

            new_dp = dp[i][k - 1] + dp[k][j] + s
            if dp[i][j] == 0 or new_dp < dp[i][j]:
                dp[i][j] = new_dp
                p[i][j] = k


print(dp[0][n - 1])
for i in range(n):
    for j in range(n):
        print(dp[i][j], end=' ')
    print()

for i in range(n):
    for j in range(n):
        print(p[i][j], end=' ')
    print()

