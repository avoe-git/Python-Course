a=int(input())
k=1
while a>0:
    k = a*k
    a -= 1
print(str(k).count('1'))