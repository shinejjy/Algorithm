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
