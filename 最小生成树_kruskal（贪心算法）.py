n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
pre = [i for i in range(n)]


def find(x):
    if x == pre[x]:
        return x
    else:
        return find(pre[x])


def join(x, y):
    fx = find(x)
    fy = find(y)
    pre[fx] = fy


for _ in range(n - 1):
    min_d = 0x3f3f3f3f
    min_i = None
    min_j = None
    for i in range(n):
        for j in range(i + 1, n):
            if find(i) != find(j):
                if min_d > A[i][j] != 0:
                    min_d = A[i][j]
                    min_i = i
                    min_j = j

    join(min_i, min_j)
    print('{} {} {}'.format(min_i + 1, min_j + 1, min_d))
