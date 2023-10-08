data = list(map(int, input().split()))
ans = 0


def Merge(l, m, r):
    global data
    new_data = []
    p1, p2 = l, m + 1
    while p1 <= m and p2 <= r:
        while data[p1] < data[p2]:
            new_data.append(data[p1])
            p1 = p1 + 1
            if p1 > m:
                break

        while data[p1] > data[p2] and p2 <= r:
            new_data.append(data[p2])
            p2 = p2 + 1
            if p2 > r:
                break

    while p1 <= m:
        new_data.append(data[p1])
        p1 = p1 + 1

    while p2 <= r:
        new_data.append(data[p2])
        p2 = p2 + 1

    data[l: r + 1] = new_data


def MergeSort(l, r):
    global ans
    ans = ans + 1
    if l >= r:
        return
    m = (l + r) // 2
    MergeSort(l, m)
    MergeSort(m + 1, r)
    Merge(l, m, r)


MergeSort(0, len(data) - 1)
print(ans)
for num in data:
    print(num, end=' ')

