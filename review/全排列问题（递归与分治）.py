data = list(map(int, input().split()))


def solve(k, m):
    if k == m:
        print(' '.join(map(str, data)))
    else:
        for i in range(k, m + 1):
            data[i], data[k] = data[k], data[i]
            solve(k + 1, m)
            data[i], data[k] = data[k], data[i]


solve(0, len(data) - 1)
