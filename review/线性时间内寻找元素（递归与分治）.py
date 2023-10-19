data = list(map(int, input().split()))
ii = int(input())
flag = 1


# 函数排序了，并找实际数组的中位数索引和中位数
def findMid(l, r):
    data[l: r + 1] = sorted(data[l: r + 1])
    return (l + r) // 2, data[(l + r) // 2]


# 这里的函数找的是根据划分中位数的中位数，k输出的是事迹数组的索引
def findK(l, r) -> int:
    n_group = (r - l + 1) // 5
    for group in range(0, n_group):
        index, Mid = findMid(l + 5 * group, l + 5 * (group + 1) - 1)
        data[index], data[l + group] = data[l + group], data[index]  # 把中位数都放前面去

    index, Mid = findMid(l, l + n_group)  # 找到排在前面的中位数的中位数
    data[index], data[r] = data[r], data[index]  # 让其和r交换
    global flag
    if flag:
        print(Mid)
        flag = 0

    k = l  # 接下来的操作和快速排序一致，k其实就是大于中间值的左界，如果j移动找到比中间值小的数，让其和i交换，i++即可，相当于把小的那个扩大了
    for j in range(l, r):
        if data[j] < data[r]:
            data[k], data[j] = data[j], data[k]
            k = k + 1

    data[k], data[r] = data[r], data[k]

    return k


# 函数寻找的是实际数组索引下，第i大的数
def Search(l, r, i):
    # 当规模小于等于5时，直接进行排序
    if r - l + 1 <= 5:
        data[l: r + 1] = sorted(data[l: r + 1])
        return data[l + i - 1]  # i表示的是当前索引下，第i大的数组，所以需要从l加，并且由于索引和大小的原因，需要-1

    k = findK(l, r)  # 当规模较大时，需要找适合的k，这里的k和快速排序一样，指的是真实数组索引
    sub_k = k - l + 1  # sub_k表示的是找到的索引为k的这个数在l~r之间是第几个大，比如索引为l，l-l+1=1
    if i == sub_k:  # 一致时，直接返回
        return data[k]
    elif i < sub_k:  # 小时，好理解
        return Search(l, k - 1, i)
    else:  # 大时，需要注意i-sub_k，要找第i大，但我们已经找到了第sub_k大，我们只要找右边元素的第i-sub_k大即可，比如找到了8大，要9大，即剩1大
        return Search(k + 1, r, i - sub_k)


print(Search(0, len(data) - 1, ii))
print(data)
