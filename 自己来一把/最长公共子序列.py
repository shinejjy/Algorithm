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
