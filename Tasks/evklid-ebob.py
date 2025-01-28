l = list(map(int, input().split()))
def ebob(a, b):
    if b == 0:
        return a
    else:
        return ebob(b, a % b)
ebob_o=ebob(l[0],l[1])
for i in range(2, len(l)):
    ebob_o=ebob(ebob_o, l[i])
    if ebob_o==1:
        print(ebob_o)
        break
print(ebob_o)