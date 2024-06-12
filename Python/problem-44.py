'''
44. s=['aa', 17, 'bb', 45, 'cc', 128, '1c', 25] siyahısı verilmişdir. Dövr
operatorundan istifadə etməklə verilmiş siyahının tam ədəd olan
elementlərininin ayrı-ayrılıqda rəqəmləri hasilini ekranda əks etdirən
proqram tərtib edin.
'''

s=['aa', 17, 'bb', 45, 'cc', 128, '1c', 25]
v=[]
for i in s:
    if type(i) == int:
        g=1
        for k in str(i):
            g = g * int(k)
        v.append(g)
print(v)