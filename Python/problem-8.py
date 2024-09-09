'''
8. Mağazaya daxil olan ilk 50 ədəd malın qiymətini siyahıya əlavə edən
və sonda onların cəmini ekranda əks etdirən proqram tərtib edin.
'''
x=[]
for i in range(50):
    a = int(input())
    x.append(a)
print(sum(x))