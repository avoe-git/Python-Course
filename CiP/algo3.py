n = int(input())
k = 0
i = 3
j = 0
isP = False
if 999 < n < 10000:
    while k < 10000:
        k += ((n//10**i) % 10) * (10**j)
        i -= 1
        j += 1
        if k == n:
            isP = True
            break
    if isP:
        print('YES')
    else:
        print('NO')
        