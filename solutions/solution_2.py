"""
Solution for problem #2 [Generated by avoe's afs.py]

Statement of the problem:
Klaviaturadan daxil edilmiş n sayda müsbət ədədlər ardıcıllığının bütün üçlüklərinin (yanaşı gələn 3 element) arasında itibucaqlı üçbucağın tərəfləri ola bilənlərin sayını müəyyən edən proqramı yazın. (Qeyd: Üçbucağın ən böyük tərəfinin kvadratı onun digər tərəflərinin kvadratları cəmindən kiçik olarsa, o itibucaqlıdır)
"""

n = int(input("Neçə ədəd daxil edilsin: "))
k = []
temp = []
üçbucaqlar = []
say = 0
while n > 0:
    k.append(int(input("Növbəti ədəd: ")))
    n -= 1
for i in k:
    if k.index(i)+2 >= len(k):
        continue
    else:
        temp.append(i**2)
        temp.append(k[k.index(i)+1]**2)
        temp.append(k[k.index(i)+2]**2)
        temp.sort()
    if temp[0] + temp[1] == temp[2]:
        say += 1
        üçbucaqlar.append(temp)
    temp = []
print("Qurula biləcək itibucaqlı üçbucaqların sayı:" , say , "\nBu itibucaqlı üçbucaqların tərəflərinin kvadratları:" ,üçbucaqlar)

#* Completed