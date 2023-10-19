data = list(map(int, input().split()))
ans = 0


def Merge(begin, end, mid):
    a = data[begin: mid + 1]
    b = data[mid + 1: end + 1]
    a.append(0x3f3f3f3f)
    b.append(0x3f3f3f3f)
    p1, p2 = 0, 0
    for k in range(begin, end + 1):
        if a[p1] < b[p2]:
            data[k] = a[p1]
            p1 = p1 + 1
        else:
            data[k] = b[p2]
            p2 = p2 + 1


def MergeSort(begin, end):
    global ans
    ans = ans + 1
    if end > begin:
        mid = (begin + end) // 2
        MergeSort(begin, mid)
        MergeSort(mid + 1, end)
        Merge(begin, end, mid)


MergeSort(0, len(data) - 1)
print(ans)
print(' '.join(map(str, data)))
