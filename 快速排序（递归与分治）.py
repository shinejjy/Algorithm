data = list(map(int, input().split()))
ans = 0


def Partition(l, r) -> int:
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
        q = Partition(l, r)
        QuickSort(l, q - 1)
        QuickSort(q + 1, r)


QuickSort(0, len(data) - 1)
print(ans)
for num in data:
    print(num, end=' ')

"""
    48 38 65 97 76 13 27
    
"""