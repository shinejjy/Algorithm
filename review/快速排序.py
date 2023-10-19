data = list(map(int, input().split()))
ans = 0


def Partition(l, r):
    i = l
    for j in range(l, r):
        if data[j] < data[r]:
            data[i], data[j] = data[j], data[i]
            i = i + 1

    data[i], data[r] = data[r], data[i]

    return i


def QuickSort(l, r):
    global ans
    ans = ans + 1
    if r > l:
        k = Partition(l, r)
        QuickSort(l, k - 1)
        QuickSort(k + 1, r)


QuickSort(0, len(data) - 1)
print(ans)
print(' '.join(map(str, data)))
