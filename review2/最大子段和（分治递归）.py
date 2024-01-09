a = list(map(int, input().split()))


def divide_max_sub_sum(a, l, r):
    if l == r:
        return [l, r, a[l]]

    m = (l + r) // 2
    l_state = divide_max_sub_sum(a, l, m)
    r_state = divide_max_sub_sum(a, m + 1, r)

    s1 = a[m]
    l_sum = s1
    l3 = m
    for i in range(m - 1, l - 1, -1):
        l_sum += a[i]
        if l_sum > s1:
            s1 = l_sum
            l3 = i

    s2 = a[m + 1]
    r_sum = s2
    r3 = m + 1
    for i in range(m + 2, r + 1):
        r_sum += a[i]
        if r_sum > s2:
            s2 = r_sum
            r3 = i

    m_max = s1 + s2
    m_state = [l3, r3, m_max]

    return sorted([l_state, r_state, m_state], key=lambda x: x[2], reverse=True)[0]


l, r, all_max = divide_max_sub_sum(a, 0, len(a) - 1)
print(f'{all_max}\n{l + 1}\n{r + 1}')
