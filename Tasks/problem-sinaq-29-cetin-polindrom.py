a = list(input().split(' '))
f=[]
g=[]
m=1
d=1
em=0
me=0
for i in range(len(a)):
    if a[i] == a[i][::-1]:
        f.append(len(a[i]))
    else:
        g.append(len(a[i]))

for i in f:
    s=0
    for j in range(2,i):
        if i%j ==0:
            s+=1
    if s==0:
        em+=1

for i in g:
    s=0
    for j in range(2,i):
        if i%j ==0:
            s+=1
    if s!=0:
        me+=1
print(me*em)