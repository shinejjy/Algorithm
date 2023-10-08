def print_list(sub_data: list):
    for num in sub_data:
        print(num, end=' ')
    print()
    return


data = list(map(int, input().split()))
key = int(input())

lens = len(data)

l = 0
r = lens - 1
f = 0
while l <= r:
    print_list(data[l: r + 1])
    if key < data[l] or key > data[r]:
        break
    m = (l + r) // 2
    if data[m] == key:
        print(m + 1)
        f = 1
        break
    elif data[m] > key:
        r = m - 1
    else:
        l = m + 1

if not f:
    print(0)