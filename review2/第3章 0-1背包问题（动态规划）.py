import numpy as np

ans = []


def search_ans(dp, c, n, ans_list):
    if n == 1:
        if c >= w[0]:
            ans_list_new = [n] + ans_list
        ans.append(ans_list_new)
        return
    if dp[n][c] == dp[n - 1][c]:
        if c >= w[n - 1]:
            if dp[n - 1][c - w[n - 1]] + v[n - 1] == dp[n][c]:
                ans_list_new = [n] + ans_list
                search_ans(dp, c - w[n - 1], n - 1, ans_list_new)

            search_ans(dp, c, n - 1, ans_list)
    else:
        ans_list_new = [n] + ans_list
        search_ans(dp, c - w[n - 1], n - 1, ans_list_new)


c = int(input())
n = int(input())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, c + 1):
        if w[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

# print(np.array(dp))
print(dp[n][c])
search_ans(dp, c, n, [])

if len(ans) == 1:
    print(' '.join(map(str, ans[0])))
else:
    print(' '.join(map(str, ans[1])))

"""
10
5
6 3 5 4 6
2 2 6 5 4
"""
