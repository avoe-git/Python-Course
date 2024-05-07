'''
42. Verilmiş sətirdə (mətndə) ən qısa və ən uzun sözü müəyyənləşdirən
proqram yazın.
'''

a = list(input().split(' '))
k=[]
for i in range(len(a)):
    k.append(len(a[i]))

print(a[k.index(max(k))] , a[k.index(min(k))])