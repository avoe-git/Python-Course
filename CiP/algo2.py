n = int(input())
x = n // 100
y = n // 10 - x * 10
z = n - x * 100 - y * 10
if 99 < n < 1000:
    if n == x**3 + y**3 + z**3:
        print('CONGRATS!')
    else:
        print('NO')
else:
    print('ERROR')