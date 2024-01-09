a = list(map(int, input().split()))
b = 0
best = -float('inf')
best_l = best_r = 0

l = r = 0
for i in range(len(a)):
    r = i
    if b > 0:
        b += a[i]
    else:
        l = i
        b = a[i]

    if b > best:
        best = b
        best_l = l
        best_r = r

print(best)
print(best_l + 1)
print(best_r + 1)

