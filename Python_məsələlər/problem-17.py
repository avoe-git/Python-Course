'''
17. 1000-ə qədər Fibonaççi sırasına daxil olan bütün ədədləri ekranda əks etdirən proqram tərtib edin.
'''
f = 1
f2 = 1
while True:
    f=f2+f
    f2=f+f2
    if f<1000 or f2<1000:
        print(f,'\n',f2)
    else:
        break
