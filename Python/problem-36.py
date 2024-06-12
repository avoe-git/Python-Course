'''
36. Sətirdə boşluqları və təkrarlanan simvolları silib çıxışa verin.
Məsələn, əgər "abc cde def" sətri daxil edilmişsə, onda çıxışa "abcdef"
sətri verilməlidir.
'''

listed = list(input())

for i in listed:
    if listed.count(i)>1 and i !=' ':
        o=1
        while listed.count(i) != 1 and listed.index(i)+o < len(listed):
            if listed[listed.index(i) + o] == i:
                del listed[listed.index(i)+o]
            o+=1

print(''.join(filter(lambda x: x!=' ',listed)))