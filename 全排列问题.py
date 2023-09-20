import copy

def solve(li ,begin, end):
    if begin == end:
        print(" ".join(li))
    else:
        for i in range(begin, end + 1):
            li[begin], li[i] = li[i], li[begin]
            solve(li, begin + 1, end)
            li[begin], li[i] = li[i], li[begin]

ns = list(map(str, input().split()))
solve(ns, 0, len(ns) - 1)