'''
41. Mətndə durğu işarələrindən sonra qoyulmamış boşluğu
müəyyənləşdirib uyğun səhvləri düzəldən proqram yazın. Durğu
işarəsindən sonra bir boşluq qoyulmalıdır.
Proqramı üç durğu işarəsi üçün ( ":", "," , ".") belə yazmaq olar:
'''

durgu_isareleri=['.',':',',']
metn = list(input())
yeni = []
for i in metn:
    if i not in durgu_isareleri or not ' ':
        yeni.append(i)
    elif i in durgu_isareleri:
        yeni.append(i)
        yeni.append(' ')
print(''.join(yeni))