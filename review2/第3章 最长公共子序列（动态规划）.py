import copy

import numpy as np

X = input().split()
Y = input().split()
lenX = len(X)
lenY = len(Y)

c = np.full((lenX + 1, lenY + 1), np.inf)
s = [['' for _ in range(lenY + 1)] for _ in range(lenX + 1)]

for i in range(lenX + 1):
    c[i, 0] = 0
for j in range(lenY + 1):
    c[0, j] = 0


def solve(i, j):
    if c[i, j] != np.inf:
        return c[i, j], s[i][j]
    if X[i - 1] == Y[j - 1]:
        pre_c, pre_s = solve(i - 1, j - 1)
        c[i, j] = pre_c + 1
        s[i][j] = pre_s + X[i - 1]
        return c[i, j], s[i][j]
    else:
        pre_c1, pre_s1 = solve(i - 1, j)
        pre_c2, pre_s2 = solve(i, j - 1)
        if pre_c1 < pre_c2:
            c[i, j] = pre_c2
            s[i][j] = pre_s2
        else:
            c[i, j] = pre_c1
            s[i][j] = pre_s1
        return c[i, j], s[i][j]


ans_c, ans_s = solve(lenX, lenY)
print(int(ans_c))
print(ans_s if int(ans_c) != 0 else None)
"""
A B C B D A B
B D C A B A
"""
