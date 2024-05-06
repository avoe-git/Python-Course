'''
38. a = [2, 5, –49, 7, –4, 98, 30, 6] siyahısında 7-yə tam bölünən
elementləri və onların indekslərini müəyyən edən proqramı dövr
operatorundan istifadə etməklə qurun.
'''

a = [2, 5, -49, 7, -4, 98, 30 , 6]
x=[]
for i in a: 
    if i%7==0:
        x.append(str(a.index(i)))
print(' '.join(x))