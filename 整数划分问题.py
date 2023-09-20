import copy
def solve(now:list, sheng: int):
    if sheng == 0:
        global ans, cnt
        anss.append(' '.join(list(map(str, now))))
        cnt = cnt + 1
        return
    if not now:
        begin = n
    else:
        begin = min(sheng, now[-1])
    for i in range(begin, 0, -1):
        new = copy.deepcopy(now)
        new.append(i)
        solve(new, sheng - i)


n = int(input())
cnt = 0
anss = []
solve([], n)
print(cnt)
for ans in anss:
    print(ans)
