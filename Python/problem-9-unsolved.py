import math
'''
9. n sayda tam ədəd verilib. Onların içərisində elə iki ədəd tapın ki,
ƏBOB qiyməti ən böyük olsun.


UNSOLVED
'''

a = int(input('say: '))
f =[]
yoxla=[]
for i in range(a):
    x = int(input())
    f.append(x)
for d in range(len(f)):
    fd = f[d]
    for g in range(len-d):
        yoxla.append(math.gcd(f[d],f[d+g]))
        print(yoxla, 'test')
    