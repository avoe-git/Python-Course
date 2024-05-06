'''
39. Verilmiş ədədlər siyahısında 0-a bərabər elementləri maksimal
element ilə əvəz edən proqram qururn.
'''

k = list(map(int,input('Ədədlər siyahısını boşluqlarla daxil edin\n').split(' ')))
for i in k:
    if i == 0:
        k[k.index(i)] = max(k)

print(k)