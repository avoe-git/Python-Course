'''
40. Verilmiş siyahının tək indeksli elementlərini onların qiymətləi ilə
siyahının minimal elementinin cəmindən alınan ədələrlə əvəz dən
proqram qurun.
'''

k = list(map(int,input('Ədədlər siyahısını boşluqlarla daxil edin\n').split(' ')))

for i in range(len(k)):
    if i%2!=0:
        k[i] = k[i] + min(k)

print(k)