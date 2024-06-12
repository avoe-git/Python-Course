n = int(input())
b=[]
x=0
for i in range(10,n):
    listo = list(str(i))
    listok = listo.copy()
    listok.sort()
    if listok==listo:
        x += 1
print(x)