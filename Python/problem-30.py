'''
30. Yazı qaydalarına görə, mətndə vergüldən sonra həmişə boşluq
qoyulur. Aşağıdakı proqram əgər vergüldən sonra boşluq yoxdursa
həmin yerə boşluq əlavə edir.
'''

a = list(input())
for i in range(len(a)):
    if a[i]==',':
        if a[i+1]!=' ':
            a.insert(i+1,' ')
            
print(''.join(a))