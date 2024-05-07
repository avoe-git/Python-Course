'''
43. Daxil edilmiş natural ədədin 1-ci və sonuncu rəqəmlərinin yerini
dəyişən proqram tərtib edin.
'''

k = list(input())
a1 = k[0] 
a2 = k[len(k)-1]
k[len(k)-1] = a1
k[0] = a2
print(''.join(k))