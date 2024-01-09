a = list(map(int, input().split()))

b = 0
summ = 0
l = r = 0
best_l = best_r = 0
for i in range(len(a)):
    if b > 0:
        b += a[i]
        r = i
    else:
        b = a[i]
        l = r = i

    if b > summ:
        summ = b
        best_l = l
        best_r = r

print(f'{summ}\n{best_l + 1}\n{best_r + 1}')
