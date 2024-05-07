'''
41. Mətndə durğu işarələrindən sonra qoyulmamış boşluğu
müəyyənləşdirib uyğun səhvləri düzəldən proqram yazın. Durğu
işarəsindən sonra bir boşluq qoyulmalıdır.
Proqramı üç durğu işarəsi üçün ( ":", "," , ".") belə yazmaq olar:
'''

durgu_isareleri=['.',':',',']
metn = list(input())
me=[]
for i in metn:
    if i in durgu_isareleri:
        if metn[metn.index(i)+1] != ' ':
            me.append(metn.index(i)+1)

for i in range(len(me)):
    metn.insert(me[i]+i,' ')

print(''.join(metn))