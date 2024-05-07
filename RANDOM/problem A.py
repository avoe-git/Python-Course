a = int(input())
b=1
e=0

for i in range(a//2):
    b+=1
    c=a
    d=a
    while c>1:
        c=d/b
        d=d/b
        if c==1:
            print(b)
            c+=1
            e+=1

if e==0:
    print('no')