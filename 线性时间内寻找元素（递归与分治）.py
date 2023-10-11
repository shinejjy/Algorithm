data = list(map(int, input().split()))
i = int(input())
flag = True


def partition(n, l, r):

    medians = []
    n_groups = n // 5
    for group in range(n_groups):
        temp = list(enumerate(data[l + group * 5: l + (group + 1) * 5]))
        temp = [[x[0] + l + group * 5, x[1]] for x in temp]
        temp = sorted(temp, key=lambda x: x[1])
        medians.append(temp[2])

    medians = sorted(medians, key=lambda x: x[1])
    k = medians[(n_groups - 1) // 2][0]

    global flag
    if flag:
        print(data[k])
        flag = False

    data[k], data[r] = data[r], data[k]

    ii = l
    for jj in range(l, r):
        if data[jj] < data[r]:
            data[ii], data[jj] = data[jj], data[ii]
            ii = ii + 1

    data[ii], data[r] = data[r], data[ii]

    return ii


def select(l, r, i):
    """
    :param l: left
    :param r: right
    :param i: find number index in data[l...r]
    :return:
    """
    n = r - l + 1
    if n <= 5:
        data[l: r + 1] = sorted(data[l: r + 1])
        return data[l + i - 1]

    q = partition(n, l, r)

    k = q - l + 1
    if i == k:
        return data[q]
    elif i < k:
        return select(l, q - 1, i)
    else:
        return select(q + 1, r, i - k)


print(select(0, len(data) - 1, i))
"""
2 9 8 0 7 10 1 12 3 14 5 13 6 11 4
"""